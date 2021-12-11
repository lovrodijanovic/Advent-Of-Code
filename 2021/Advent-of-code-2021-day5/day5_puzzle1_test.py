# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:09:24 2021

@author: Loc
"""

import re

lines = []
with open('test.txt') as f:
    lines = f.readlines()
f.close()


x1 = []
y1 = []
x2 = []
y2 = []
for i in range(0,10):
    line = re.split(', |-> |,',lines[i])
    x1.append(int(line[0]))       
    y1.append(int(line[1]))
    x2.append(int(line[2]))
    y2.append(int(line[3]))

array2d = [ [0] * 10 for _ in range(10)]

           
for i in range(0,10):
    if((x1[i] == x2[i]) or (y1[i] == y2[i])):
        array2d[x1[i]][y1[i]] = 1
        array2d[x2[i][y2[i]]] = 1

            
