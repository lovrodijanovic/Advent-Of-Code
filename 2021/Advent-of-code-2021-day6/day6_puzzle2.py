# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:35:31 2021

@author: Loc
"""
days = 256

initialStates = []
with open('input.txt') as f:
    lines = f.readline()  
    initialStates = lines.split(",")
f.close()

initialStates = list(map(int, initialStates))

allStates = [0] * 9

#setting initial state
for i in range(0, 9):
    counter = 0
    for j in range(0, len(initialStates)):
        if(initialStates[j] == i):
            counter += 1
    if(counter == 0):
        continue
    else:
        allStates[i] = counter        


six = 0
for i in range(0, days):
    for j in range(1, len(allStates)):       
        temp = allStates[j]
        allStates[j] = allStates[j-1]
        allStates[j-1] = temp
    allStates[6] = six
    six = allStates[0] + allStates[7]  

finalSum = 0        
for i in range(0, len(allStates)):
    finalSum += allStates[i]

print(finalSum)