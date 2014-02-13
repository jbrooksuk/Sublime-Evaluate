# Sublime Evaluate [![Gittip](http://badgr.co/gittip/jbrooksuk.png)](https://www.gittip.com/jbrooksuk/)
A powerful plugin which returns the value of selected regions.

# Evaluation Environment
Sublime Evaluate is able to evaluate the `math` and `datetime` import as part of its enviroment. This opens up access to a whole range of Python functions such as:

```python
math.atan2(80, 40)

math.pi * 60

datetime.date(2013,4,2) # Returns a formatted date

datetime.date.today()
```

We can also perform morecomplex expressions such as:

```python
(math.pi * 2) / math.pi * 0.5
```

# License
MIT - [http://jbrooksuk.mit-license.org](http://jbrooksuk.mit-license.org)
