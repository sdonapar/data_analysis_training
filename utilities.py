#!/usr/bin/env python

def my_dir(mylist):
    import re
    pattern = re.compile('_[0-9a-z]+')
    return [x for x in mylist if not pattern.match(x) and x not in ('In','Out','_','__','___','exit','quit','get_ipython')] 

def hello(name):
    return "Hello " + name + ", How are you ?"
