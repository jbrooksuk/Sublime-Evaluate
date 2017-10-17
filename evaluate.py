from __future__ import division
import sublime
import sublime_plugin
import threading
import math
import datetime
import subprocess

sublime_version = 2

if not sublime.version() or int(sublime.version()) > 3000:
    sublime_version = 3

class EvaluateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()

        threads = []
        for sel in sels:
            to_eval = self.view.substr(sel)
            thread = EvaluateCall(sel, to_eval, 5)
            threads.append(thread)
            thread.start()

        self.view.sel().clear()
        if sublime_version == 2:
            edit = self.view.begin_edit('evaluate')

        self.handle_threads(edit, threads)

        if sublime_version == 2:
            self.view.end_edit(edit)

    def handle_threads(self, edit, threads, offset=0):
        for t in threads:
            t.join(5) # TODO: use bulk join maybe
            offset = self.replace(edit, t, offset)

        selections = len(self.view.sel())
        sublime.status_message('Evaluated %s selection%s!' % (selections, '' if selections == 1 else 's'))

    def replace(self, edit, thread, offset):
        sel = thread.sel
        original = thread.original
        result = thread.result

        if offset:
            sel = sublime.Region(sel.begin() + offset, sel.end() + offset)

        prefix = original
        main = str(result)
        self.view.replace(edit, sel, main)

        end_point = (sel.begin() + len(prefix) + len(main)) - len(original)
        self.view.sel().add(sublime.Region(end_point, end_point))

        return offset + len(main) - len(original)


class EvaluateCall(threading.Thread):
    def __init__(self, sel, to_eval, timeout):
        self.sel = sel
        self.original = to_eval
        self.timeout = timeout
        self.result = self.original  # Default result
        threading.Thread.__init__(self)

    def run(self):
        '''Evaluate `self.original`, save to `self.result`.
        If `self.timeout` reached, the run fails and nothing change.

        If `self.original` starts with '!', after trimming leading spaces,
        it is evaluated as Shell code. (The same convention as ipython).

        Otherwise, it is evaluated as Python code.'''

        if self.original.lstrip().startswith('!'):
            # Remove the first bang
            shell_code = self.original.lstrip()[1:]
            try:
                p = subprocess.Popen(shell_code,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
                # stderr goes to stdout
                out, _ = p.communicate(timeout=self.timeout)
                # ad-hoc Python 2/3 str/bytes handling
                if type(out) == bytes:
                    out = out.decode()

                # Remove the last newline
                if out.endswith('\n'):
                    out = out[:-1]

                self.result = out
            except (Exception):
                # TODO: print error to console
                pass
        else:
            try:
                tmp_global = {
                    "math": math,
                    "datetime": datetime
                }
                code = compile(self.original, '<string>', 'eval')
                self.result = eval(code, tmp_global)
            except (ValueError, SyntaxError):
                pass
