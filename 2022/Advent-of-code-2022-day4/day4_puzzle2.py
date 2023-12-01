# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:42:07 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sum = 0

for i in range(0, len(lines)):
    ranges = lines[i].split(',')
    firstRange = ranges[0].split('-')
    secondRange = ranges[1].split('-')
    firstNumOfFirstRange = int(firstRange[0])
    secondNumOfFirstRange = int(firstRange[1])
    firstNumOfSecondRange = int(secondRange[0])
    secondNumOfSecondRange = int(secondRange[1])
    
    if(secondNumOfFirstRange < firstNumOfSecondRange):
        continue
    elif(firstNumOfFirstRange > secondNumOfSecondRange):
        continue
    else:
        sum += 1