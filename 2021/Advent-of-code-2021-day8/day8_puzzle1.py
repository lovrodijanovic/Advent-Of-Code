# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:41:40 2021

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

outputValues = []
for i in range(len(lines)):
    outputValues.append(lines[i].partition('| ')[2].split())

uniqueSegmentDigitsCount = 0
for i in range(len(outputValues)):
    for j in range(len(outputValues[i])):
        if(len(outputValues[i][j]) == 2 or len(outputValues[i][j]) == 3 or len(outputValues[i][j]) == 4 or len(outputValues[i][j]) == 7):
            uniqueSegmentDigitsCount += 1
print(uniqueSegmentDigitsCount)