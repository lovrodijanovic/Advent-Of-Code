# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:03:25 2021

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
        if(int(values[j]) < i):
            n = i - int(values[j])
            fuelSum += (n * (n + 1)) / 2
        elif(int(values[j]) > i):
            n = int(values[j]) - i
            fuelSum += (n * (n + 1)) / 2
        else:
            fuelSum += 0
    if(fuelSum < lowest_fuel_cost):
        lowest_fuel_cost = fuelSum
        
print(lowest_fuel_cost)