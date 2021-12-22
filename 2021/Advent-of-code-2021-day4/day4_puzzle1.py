# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:10:41 2021

@author: Loc
"""

lines = []
with open('input.txt') as f:
    lines = f.readlines()
f.close()


winningNumbers = lines[0].split(",")


lines = [x for x in lines if x != "\n"] 
lines.remove(lines[0])

for i in range(0,len(lines)):
    lines[i] = lines[i].split()

boards = []
rows = []

while(len(lines) > 0):
    i = 0
    while(i <= 4):
        rows.append(lines[0])
        lines.remove(lines[0])
        i += 1
    boards.append(rows)
    rows = []
        

turnCounter = []
scores = []
flag = 0
for i in range(0, len(boards)):
    winningNumberCounter = 0
    flag = 0
    for l in range(0,len(winningNumbers)):
        if(flag == 1):
            break
        for j in range(0,len(boards[i])):
            if(flag == 1):
                break
            for k in range(0, len(boards[i][j])):
                if(boards[i][j][k] == winningNumbers[l]):
                    boards[i][j][k] = 'O'
                    winningNumberCounter += 1
                    for m in range(0,len(boards[i])):
                        countO = 0
                        for n in range(0, len(boards[i][j])):
                            if(boards[i][m][n] == 'O'):
                                countO += 1
                        if(countO == 5):
                            turnCounter.append(winningNumberCounter)
                            unmarkedSum = 0
                            for m in range(0,len(boards[i])):
                                for n in range(0, len(boards[i][j])):
                                    if(boards[i][m][n] != 'O'):
                                        unmarkedSum += int(boards[i][m][n])
                            scores.append(unmarkedSum*int(winningNumbers[l]))
                            flag = 1
                            break
                    if(flag == 1):
                        break;
                    for n in range(0,len(boards[i])):
                        countO = 0
                        for m in range(0, len(boards[i][j])):
                            if(boards[i][m][n] == 'O'):
                                countO += 1
                        if(countO == 5):
                            turnCounter.append(winningNumberCounter)
                            unmarkedSum = 0
                            for n in range(0,len(boards[i])):
                                for m in range(0, len(boards[i][j])):
                                    if(boards[i][m][n] != 'O'):
                                        unmarkedSum += int(boards[i][m][n])
                            scores.append(unmarkedSum*int(winningNumbers[l]))
                            flag = 1
                            break
                    if(flag == 1):
                        break;                            

low = turnCounter[0]
for i in range(0, len(turnCounter)):
    if(turnCounter[i] < low):
        low = turnCounter[i]
        lowIndex = i

print(scores[lowIndex])
    