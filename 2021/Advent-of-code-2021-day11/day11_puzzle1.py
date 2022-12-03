# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:17:20 2021

@author: Loc
"""
steps = 100


def flash(i, j, counter, matrix):    
    if(matrix[i][j] <= 9):
        return        
    counter += 1
    if(matrix[i+1][j] != None):
        matrix[i+1][j] += 1
    if(matrix[i-1][j] != None):
        matrix[i-1][j] += 1
    if(matrix[i][j+1] != None):
        matrix[i][j+1] += 1
    if(matrix[i][j-1] != None):
        matrix[i][j-1] += 1
    if(matrix[i+1][j+1] != None):
        matrix[i+1][j+1] += 1    
    if(matrix[i+1][j-1] != None):
        matrix[i+1][j-1] += 1    
    if(matrix[i-1][j+1] != None):
        matrix[i-1][j+1] += 1   
    if(matrix[i-1][j-1] != None):
        matrix[i-1][j-1] += 1   
    flash(i+1,j, counter, matrix)
    flash(i,j+1, counter, matrix)
    flash(i-1,j, counter, matrix)
    flash(i,j-1, counter, matrix)
    flash(i-1,j-1, counter, matrix)
    flash(i+1,j+1, counter, matrix)
    flash(i-1,j+1, counter, matrix)
    flash(i+1,j-1, counter, matrix)

with open('small-test.txt') as f:
    lines = f.readlines()
f.close()

matrix = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    a_list = [num for num in lines[i]]
    map_object = map(int, a_list)
    matrix.append(list(map_object))

counter = 0
for step in range(steps):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] > 9):
                flash(i, j, counter, matrix)
                matrix[i][j] = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] > 9):
                matrix[i][j] = 0
print(counter)