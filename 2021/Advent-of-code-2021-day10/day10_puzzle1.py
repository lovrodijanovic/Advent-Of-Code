# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:24:14 2021

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

score = 0
for i in range(len(lines)):
    line = []
    for j in range(len(lines[i])):
        if(lines[i][j] == '(' or lines[i][j] == '[' or lines[i][j] == '{' or lines[i][j] == '<'):
            line.append(lines[i][j])
                
        if(lines[i][j] == ')' or lines[i][j] == ']' or lines[i][j] == '}' or lines[i][j] == '>'):
            last = line[-1]
            if((lines[i][j] == ')' and last == '(') or (lines[i][j] == ']' and last == '[') or (lines[i][j] == '}' and last == '{') or (lines[i][j] == '>' and last == '<')):
                line.pop()
                continue
            else:
                if(lines[i][j] == ')'):
                    score += 3
                    break
                elif(lines[i][j] == ']'):
                    score += 57
                    break
                elif(lines[i][j] == '}'):
                    score += 1197
                    break
                elif(lines[i][j] == '>'):
                    score += 25137
                    break
            
print(score)        
