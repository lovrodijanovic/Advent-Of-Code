# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:09:24 2021

@author: Loc
"""
import re

with open('input.txt') as f:
    lines = f.readlines()
f.close()

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(0,len(lines)):
    line = re.split(', |-> |,',lines[i])
    x1.append(int(line[0]))       
    y1.append(int(line[1]))
    x2.append(int(line[2]))
    y2.append(int(line[3]))

diagram = [ [0] * 1000 for _ in range(1000)]
           
for i in range(0,len(lines)):
    if(y1[i] == y2[i]):
        if(x1[i] < x2[i]):
            for j in range(x1[i],x2[i]+1):
                diagram[y1[i]][j] += 1
        else:
            x1[i],x2[i] = x2[i],x1[i]
            for j in range(x1[i],x2[i]+1):
                diagram[y1[i]][j] += 1
    if(x1[i] == x2[i]):
        if(y1[i] < y2[i]):
            for j in range(y1[i],y2[i]+1):
                diagram[j][x1[i]] += 1
        else:
            y1[i],y2[i] = y2[i],y1[i]
            for j in range(y1[i],y2[i]+1):
                diagram[j][x1[i]] += 1

overlapCount = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if(diagram[i][j] > 1):
            overlapCount += 1
print(overlapCount)








