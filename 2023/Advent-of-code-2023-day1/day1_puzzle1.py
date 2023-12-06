# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:27:06 2023

@author: Loc
"""

with open('input.txt') as file:
    lines = file.readlines()
file.close()

result = 0;

for i in range(len(lines)):
    string = filter(str.isdecimal, lines[i])
    numbers = "".join(string)
    if len(numbers) == 1:
        result += int(2 * numbers)
    else:
        result += int(numbers[0] + numbers[len(numbers) - 1])
