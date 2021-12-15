# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:35:24 2021

@author: Loc
"""

days = 80

initialStates = []
with open('test.txt') as f:
    lines = f.readline()  
    initialStates = lines.split(",")
f.close()

initialStates = list(map(int, initialStates))

flag = 0
for i in range(0, days): 
    for j in range(0, len(initialStates)):
        if(initialStates[j] == 0):
            initialStates[j] = 6
            initialStates.append(8)
        else:
            initialStates[j] -= 1
    
print(len(initialStates))