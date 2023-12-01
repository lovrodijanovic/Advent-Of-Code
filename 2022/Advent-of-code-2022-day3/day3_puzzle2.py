# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:23:10 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sum = 0
lowerLettersCoeficiant = 96
capitalLettersCoeficiant = 38
commonItem = ''

for i in range(1, len(lines)+1):
    if(i%3 == 0):
        firstLine = lines[i-3].strip()
        secondLine = lines[i-2].strip()
        thirdLine = lines[i-1].strip()
        strings = [firstLine, secondLine, thirdLine]
        commonItem = list(set.intersection(*map(set, strings)))
        if(commonItem[0].isupper()):
            sum += ord(commonItem[0]) - capitalLettersCoeficiant
        elif(commonItem[0].islower()):
            sum += ord(commonItem[0]) - lowerLettersCoeficiant