# -*- coding: utf-8 -*-

lines = []
with open('input.txt') as f:
    lines = f.readlines()
    
for i in range(0,12):
    ones = 0
    zeros = 0
    for j in range(len(lines)):
        if(lines[i][j] == '1'):
            ones += 1
        else:
            zeros += 1
    if(ones > zeros):
        if(lines[i][0] == 0):
            lines.remove(lines[i][0])
    