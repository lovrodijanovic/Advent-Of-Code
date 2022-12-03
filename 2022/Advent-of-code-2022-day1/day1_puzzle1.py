# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:37:12 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

max = 0;
sum = 0;

for i in range(0,len(lines)):
    if(lines[i] != '\n'):
        sum = sum + int(lines[i])
    else:
        if(sum > max):
            max = sum
        sum = 0
        