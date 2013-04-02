# Sublime Evaluate
This plugin evaluates current selections.

# Evaluation Environment
Sublime-Evaluate is able to evaluate the `math` and `datetime` import as part of its enviroment. This opens up access to a whole range of Python functions such as:

    math.atan2(80, 40)

    math.pi * 60

    datetime.date(2013,4,2) # Returns a formatted date

    datetime.date.today()

We can also perform complex expressions such as:

    (math.pi * 2) / math.pi * 0.5

# Credits
All credit goes to [William Bond's Prefixr Plugin](https://github.com/wbond/sublime_prefixr) as I've only re-written and modified to understand how Will has implemented a lot of the API from Sublime that intrigues me.

# License
The MIT License (MIT)
Copyright © 2013 James Brooks, http://james.brooks.so

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.