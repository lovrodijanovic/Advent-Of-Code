# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:53:11 2022

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sum = 0
lowerLettersCoeficiant = 96
capitalLettersCoeficiant = 38
commonItem = ''

for i in range(0, len(lines)):
    firstpart, secondpart = lines[i][:len(lines[i])//2], lines[i][len(lines[i])//2:]
    commonItem = list(set(firstpart)&set(secondpart))
    if(commonItem[0].isupper()):
        sum += ord(commonItem[0]) - capitalLettersCoeficiant
    elif(commonItem[0].islower()):
        sum += ord(commonItem[0]) - lowerLettersCoeficiant
    
    