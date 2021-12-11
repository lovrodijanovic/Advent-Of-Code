# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:20:47 2021

@author: Loc
"""
import math


values = []
with open('input.txt') as f:
    stringOfInputs = f.readline()
    values = stringOfInputs.split(",")
f.close()

lowest_fuel_cost = math.inf
fuelSum = 0
for i in range(0,2000):
    fuelSum = 0
    for j in range(len(values)):
        fuelSum += abs(int(values[j]) - i)
    if(fuelSum < lowest_fuel_cost):
        lowest_fuel_cost = fuelSum
        
print(lowest_fuel_cost)