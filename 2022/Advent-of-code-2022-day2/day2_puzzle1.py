# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:40:54 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

rockValue = 1
paperValue = 2
scissorsValue = 3
loseValue = 0
drawValue = 3
winValue = 6
sum = 0

for i in range(0, len(lines)):
    lines[i].strip()
    if 'A X' in (lines[i]):
        sum += rockValue + drawValue
    if 'A Y' in (lines[i]):
        sum += paperValue + winValue
    if 'A Z' in (lines[i]):
        sum += scissorsValue
    if 'B X' in (lines[i]):
        sum += rockValue 
    if 'B Y' in (lines[i]):
        sum += paperValue + drawValue
    if 'B Z' in (lines[i]):
        sum += scissorsValue + winValue
    if 'C X' in (lines[i]):
        sum += rockValue + winValue
    if 'C Y' in (lines[i]):
        sum += paperValue
    if 'C Z' in (lines[i]):
        sum += scissorsValue + drawValue           