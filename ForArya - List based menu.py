# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 21:17:39 2015

@author: mj-admin
"""

a, b, c, d, e, f, g = 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg'

menus = {a: {c:{g:"acg"},d:{g:"adg"}}, b: {e:{g:"beg"}, f:{g:"bfg"}}}

currLevel = menus
moreLevels = type(currLevel) == dict
path = ""

while moreLevels:
    #print options
    selection = []
    for o in currLevel.keys():
        selection.append(o)
        print("{}: {}".format(len(selection) - 1, o))
    if (len(selection) > 1):
        x = int(input('input selection '))
    else:
        x = 0
    if selection[x] in currLevel:
        path = path + selection[x] + " --> "
        currLevel = currLevel[selection[x]]
        moreLevels = type(currLevel) == dict
        if not moreLevels:
            print("\n" + path + currLevel)


    
