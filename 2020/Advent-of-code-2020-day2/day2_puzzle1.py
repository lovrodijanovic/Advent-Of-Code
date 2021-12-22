# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 19:07:22 2021

@author: Loc
"""
import re

lines = []
with open('test.txt') as f:
    lines = f.readlines()
f.close()

inputs = []
for i in range(0, len(lines)):
    line = re.split('-|,| |:',lines[i])
    inputs.append(line)

    

counter = 0
valid = 0
for i in range(0, len(inputs)):
    for j in range(0, len(inputs[4])):
        
        
            