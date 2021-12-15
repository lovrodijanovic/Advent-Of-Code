# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:10:41 2021

@author: Loc
"""

lines = []
with open('test.txt') as f:
    lines = f.readlines()
f.close()


winningNumbers = lines[0].split(",")


for i in range(2, len(lines)):
    