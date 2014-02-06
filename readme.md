# Sublime Evaluate [![Gittip](http://badgr.co/gittip/jbrooksuk.png)](https://www.gittip.com/jbrooksuk/)
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
MIT - [http://jbrooksuk.mit-license.org](http://jbrooksuk.mit-license.org)
