# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:24:21 2021

@author: Loc
"""

with open('input.txt') as f:
    lines = f.readlines()
f.close()

score = 0
removeIndex = []
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
                    removeIndex.append(i)
                    break
                elif(lines[i][j] == ']'):
                    removeIndex.append(i)
                    break
                elif(lines[i][j] == '}'):
                    removeIndex.append(i)
                    break
                elif(lines[i][j] == '>'):
                    removeIndex.append(i)
                    break

sorted_to_remove = sorted(removeIndex, reverse = True)
for index in sorted_to_remove:
    del lines[index]

scores = []
for i in range(len(lines)):
    line = []
    for j in range(len(lines[i])):
        if(lines[i][j] == '(' or lines[i][j] == '[' or lines[i][j] == '{' or lines[i][j] == '<'):
            line.append(lines[i][j])
                
        if(lines[i][j] == ')' or lines[i][j] == ']' or lines[i][j] == '}' or lines[i][j] == '>'):
            last = line[-1]
            if((lines[i][j] == ')' and last == '(') or (lines[i][j] == ']' and last == '[') or (lines[i][j] == '}' and last == '{') or (lines[i][j] == '>' and last == '<')):
                line.pop()
                
    score = 0
    k = 1
    while(k - 1 < len(line)):
        if(line[-k] == '('):
            score *= 5
            score += 1
        elif(line[-k] == '['):
            score *= 5
            score += 2
        elif(line[-k] == '{'):
            score *= 5
            score += 3             
        elif(line[-k] == '<'):
            score *= 5
            score += 4   
        k += 1
    scores.append(score)

scores.sort()
middleIndex = int((len(scores)-1)/2)
print(scores[middleIndex])




















