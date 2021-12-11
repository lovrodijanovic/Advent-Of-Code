# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:45:43 2021

@author: Loc
"""
import re

lines = []
with open('input.txt') as f:
    lines = f.readlines()
f.close()


x1 = []
y1 = []
x2 = []
y2 = []
for i in range(0,500):
    line = re.split(', |-> |,',lines[i])
    x1.append(int(line[0]))       
    y1.append(int(line[1]))
    x2.append(int(line[2]))
    y2.append(int(line[3]))
    
