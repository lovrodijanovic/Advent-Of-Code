# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 09:06:27 2021

@author: Loc
"""
def floodFill(lowPointX, lowPointY):
    basinCounter = 0
    if(lines[lowPointX][lowPointY] == 9):
        return
    else:
        basinCounter += 1
    floodFill(lowPointX + 1, lowPointY)
    floodFill(lowPointX - 1, lowPointY)
    floodFill(lowPointX, lowPointY + 1)
    floodFill(lowPointX, lowPointY - 1)
    
lines = []
with open('test.txt') as f:
    lines = f.readlines()
f.close()

for i in range(0,len(lines)):
    lines[i] = lines[i].rstrip()

lowPoints = []
basins = []

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        
        if(i == 0 and j == 0):
            if(lines[i][j] < lines[i+1][j]):
                if(lines[i][j] < lines[i][j+1]):
                    lowPoints.append(lines[i][j])
                    basins.append(floodFill(i,j))

        elif(i == 0 and j == len(lines[i]) - 1):
            if(lines[i][j] < lines[i+1][j]):
                if(lines[i][j] < lines[i][j-1]):
                    lowPoints.append(lines[i][j])
                    basins.append(floodFill(i,j))
        elif(i == len(lines) - 1 and j == 0):
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j+1]):
                    lowPoints.append(lines[i][j])
                    basins.append(floodFill(i,j))
        elif(i == len(lines) - 1 and j == len(lines[i]) - 1):
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j-1]):
                    lowPoints.append(lines[i][j])
                    basins.append(floodFill(i,j))
                    
        elif(i == 0):
            if(lines[i][j] < lines[i+1][j]):
                if(lines[i][j] < lines[i][j+1]):
                    if(lines[i][j] < lines[i][j-1]):
                        lowPoints.append(lines[i][j])
                        basins.append(floodFill(i,j))
        elif(i == len(lines) - 1):
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j+1]):
                    if(lines[i][j] < lines[i][j-1]):
                        lowPoints.append(lines[i][j])
                        basins.append(floodFill(i,j))
        elif(j == 0):
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j+1]):
                    if(lines[i][j] < lines[i+1][j]):
                        lowPoints.append(lines[i][j])
                        basins.append(floodFill(i,j))
        elif(j == len(lines[i]) - 1):
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j-1]):
                    if(lines[i][j] < lines[i+1][j]):
                        lowPoints.append(lines[i][j])    
                        basins.append(floodFill(i,j))
        else:
            if(lines[i][j] < lines[i-1][j]):
                if(lines[i][j] < lines[i][j-1]):
                    if(lines[i][j] < lines[i+1][j]):
                        if(lines[i][j] < lines[i][j+1]):
                            lowPoints.append(lines[i][j])
                            basins.append(floodFill(i,j))
            
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        