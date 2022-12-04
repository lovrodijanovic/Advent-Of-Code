# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:42:42 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

rockValue = 1
paperValue = 2
scissorValue = 3
drawValue = 3
winValue = 6
sum = 0

for i in range(0, len(lines)):
    lines[i].strip()
    if 'A X' in (lines[i]):
        sum += scissorValue
    if 'A Y' in (lines[i]):
        sum += drawValue + rockValue
    if 'A Z' in (lines[i]):
        sum += winValue + paperValue
    if 'B X' in (lines[i]):
        sum += rockValue
    if 'B Y' in (lines[i]):
        sum += drawValue + paperValue
    if 'B Z' in (lines[i]):
        sum += winValue + scissorValue
    if 'C X' in (lines[i]):
        sum += paperValue
    if 'C Y' in (lines[i]):
        sum += drawValue + scissorValue
    if 'C Z' in (lines[i]):
        sum += winValue + rockValue  
