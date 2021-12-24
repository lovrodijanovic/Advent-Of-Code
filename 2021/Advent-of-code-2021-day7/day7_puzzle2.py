# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:03:25 2021

@author: Loc
"""
import math

with open('input.txt') as f:
    stringOfInputs = f.readline()
    values = stringOfInputs.split(",")
f.close()

lowest_fuel_cost = math.inf
fuelSum = 0

for i in range(0,2000):
    fuelSum = 0
    for j in range(len(values)):
        n = abs(int(values[j]) - i)
        fuelSum += (n * (n + 1)) / 2
    if(fuelSum < lowest_fuel_cost):
        lowest_fuel_cost = fuelSum        
print(lowest_fuel_cost)