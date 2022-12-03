# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:16:14 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sum = 0
sums = []

for i in range(0,len(lines)):
    if(lines[i] != '\n'):
        sum = sum + int(lines[i])
    else:
        sums.append(sum)
        sum = 0
        
sums.sort(reverse = True)
print(sums[0] + sums[1] + sums[2])