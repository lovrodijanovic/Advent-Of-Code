# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:48:28 2022

@author: Loc
"""
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sum = 0

def isSubArray(A, B, n, m):
    i = 0; j = 0;
    while (i < n and j < m):
        if (A[i] == B[j]):
            i += 1;
            j += 1;
            if (j == m):
                return True;
        else:
            i = i - j + 1;
            j = 0;         
    return False;

for i in range(0, len(lines)):
    ranges = lines[i].split(',')
    firstRange = ranges[0].split('-')
    secondRange = ranges[1].split('-')
    firstNumOfFirstRange = int(firstRange[0])
    secondNumOfFirstRange = int(firstRange[1])
    firstNumOfSecondRange = int(secondRange[0])
    secondNumOfSecondRange = int(secondRange[1])
    firstArray = np.arange(firstNumOfFirstRange, secondNumOfFirstRange + 1)
    secondArray = np.arange(firstNumOfSecondRange, secondNumOfSecondRange + 1)
    
    if(isSubArray(firstArray, secondArray, len(firstArray), len(secondArray))):
        sum += 1
    elif(isSubArray(secondArray, firstArray, len(secondArray), len(firstArray))):
        sum += 1
