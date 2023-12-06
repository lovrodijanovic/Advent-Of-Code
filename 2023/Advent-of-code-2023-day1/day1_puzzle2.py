# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:46:49 2023

@author: Loc
"""

with open('input.txt') as file:
    lines = file.readlines()
file.close()

words_to_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

result = 0

for i in range(len(lines) - 1):
    line = lines[i].strip()
    minimum = 0
    for key in words_to_numbers:
        print(line.find(key))
        if(line.find(key) > minimum):
            continue
        line = line.replace(key, words_to_numbers[key])
    string = filter(str.isdecimal, line)
    numbers = "".join(string)
    if len(numbers) == 1:
        result += int(2 * numbers)
    else:
        result += int(numbers[0] + numbers[len(numbers) - 1])