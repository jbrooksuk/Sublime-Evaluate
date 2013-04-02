from __future__ import division
import sublime
import sublime_plugin
import threading
import math
import datetime

sublime_version = 2

if not sublime.version() or int(sublime.version()) > 3000:
    sublime_version = 3

class EvaluateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()

        threads = []
        for sel in sels:
            string = self.view.substr(sel)
            thread = EvaluateCall(sel, string, 5)
            threads.append(thread)
            thread.start()

        self.view.sel().clear()
        if sublime_version == 2:
            edit = self.view.begin_edit('evaluate')

        self.handle_threads(edit, threads)

        if sublime_version == 2:
            self.view.end_edit(edit)

    def handle_threads(self, edit, threads, offset=0, i=0, dir=1):
        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue
            offset = self.replace(edit, thread, offset)
        threads = next_threads

        if len(threads):
            before = i % 8
            after = (7) - before
            if not after:
                dir = -1
            if not before:
                dir = 1
            i += dir
            self.view.set_status('evaluate', 'Evaluate [%s=%s]' % \
                (' ' * before, '' * after))

            sublime.set_timeout(lambda: self.handle_threads(edit, threads, offset, i, dir), 100)

            return

        self.view.erase_status('evaluate')
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

        end_point = sel.begin() + len(prefix) + len(main)
        self.view.sel().add(sublime.Region(end_point, end_point))

        return offset + len(main) - len(original)


class EvaluateCall(threading.Thread):
    def __init__(self, sel, string, timeout):
        self.sel = sel
        self.original = string
        self.timeout = timeout
        self.result = self.original  # Default result
        threading.Thread.__init__(self)

    def run(self):
        try:
            tmp_global = {
                "math": math,
                "datetime": datetime
            }
            code = compile(self.original, '<string>', 'eval')
            self.result = eval(code, tmp_global)
        except (ValueError, SyntaxError):
            pass
        return
