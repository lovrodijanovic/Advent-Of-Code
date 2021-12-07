# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:06:53 2021

@author: Loc
"""

lines = []
with open('input.txt') as f:
    lines = f.readlines()
f.close()

final_list = []

for j in range(0,12):
    ones = 0
    zeros = 0
    for i in range(len(lines)):
        if(int(lines[i][j]) == 0):
            zeros+=1
        else:
            ones+=1
    if(zeros > ones):
        final_list.append('0')
    else:
        final_list.append('1')


final_gama = ''.join(final_list)
gama = int(final_gama,2)

final_epsilon = ''.join('1' if x == '0' else '0' for x in final_gama)
epsilon = int(final_epsilon,2)

print(epsilon*gama)