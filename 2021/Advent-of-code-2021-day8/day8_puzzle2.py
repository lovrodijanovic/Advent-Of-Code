# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:41:47 2021

@author: Loc
"""
def split(word):
    return [char for char in word]

with open('input.txt') as f:
    lines = f.readlines()
f.close()

outputValues = []
signalPatterns = []
for i in range(len(lines)):
    signalPatterns.append(lines[i].partition('| ')[0].split())
    outputValues.append(lines[i].partition('| ')[2].split())

#assigning numbers
zero, one, two, three, four, five, six, seven, eight, nine= '', '', '', '', '', '', '', '', '' , '' 

grandSum = 0
for i in range(len(signalPatterns)):    
    #one,four,seven,eight
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 2):
            one = signalPatterns[i][j]
        elif(len(signalPatterns[i][j]) == 4):
            four = signalPatterns[i][j]
        elif(len(signalPatterns[i][j]) == 3):
            seven = signalPatterns[i][j]
        elif(len(signalPatterns[i][j]) == 7):
            eight = signalPatterns[i][j]

    #three
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 5):
            three = split(signalPatterns[i][j])
            one_split = split(one)
            checkThree = all(item in three for item in one_split)
            if checkThree is True:
                three = signalPatterns[i][j]
                break
    
    #nine
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 6):
            nine = split(signalPatterns[i][j])
            three_split = split(three)         
            checkNine = all(item in nine for item in three_split)
            if checkNine is True:
                nine = signalPatterns[i][j]
                break
    #zero
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 6 and signalPatterns[i][j] is not nine):
            zero = split(signalPatterns[i][j])
            one_split = split(one)         
            checkZero = all(item in zero for item in one_split)
            if checkZero is True:
                zero = signalPatterns[i][j]
                break
    
    #six
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 6 and signalPatterns[i][j] is not nine and signalPatterns[i][j] is not zero):
            six = signalPatterns[i][j]
    
    eight_set = set(eight)
    six_set = set(six)
    six_eight_diff = list(eight_set.difference(six_set))
    
    #two
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 5 and signalPatterns[i][j] is not three):
            two = split(signalPatterns[i][j])
            checkTwo = all(item in two for item in six_eight_diff)
            if checkTwo is True:
                two = signalPatterns[i][j]
                break
    
    #five
    for j in range(len(signalPatterns[i])):
        if(len(signalPatterns[i][j]) == 5 and signalPatterns[i][j] is not three and signalPatterns[i][j] is not two):
                five = signalPatterns[i][j]
                                           
    #assigning segments    
    zero_set = set(zero)
    one_set = set(one)
    two_set = set(two)
    three_set = set(three)
    four_set = set(four)
    five_set = set(five)
    six_set = set(six)
    seven_set = set(seven)
    eight_set = set(eight)
    nine_set = set(nine)
    
    up = " ".join(map(str,seven_set.difference(one_set)))
    middle = " ".join(map(str,eight_set.difference(zero_set)))
    upLeft = " ".join(map(str,nine_set.difference(three_set)))
    downLeft = " ".join(map(str,six_set.difference(five_set)))
    down = " ".join(map(str,nine_set.difference(four_set).difference(seven_set)))
    upRight = " ".join(map(str,nine_set.difference(five_set)))
    downRight = " ".join(map(str,six_set.difference(two_set).difference(upLeft)))
    
    singleResult = []
    allResults = []
    for j in range(len(outputValues[i])):
        if(len(outputValues[i][j]) == 7):
            singleResult.append(8)
        elif(len(outputValues[i][j]) == 4):
            singleResult.append(4)
        elif(len(outputValues[i][j]) == 3):
            singleResult.append(7)
        elif(len(outputValues[i][j]) == 2):
            singleResult.append(1)
        elif(len(outputValues[i][j]) == 5):
            lenFive = split(outputValues[i][j])
            two = split(two)
            three = split(three)
            five = split(five)
            checkTwo = all(item in two for item in lenFive)
            checkThree = all(item in three for item in lenFive)
            checkFive = all(item in five for item in lenFive)
            if checkTwo is True:
                singleResult.append(2)
            if checkThree is True:
                singleResult.append(3)
            if checkFive is True:
                singleResult.append(5)
        elif(len(outputValues[i][j]) == 6):
            lenSix = split(outputValues[i][j])
            zero = split(zero)
            six = split(six)
            nine = split(nine)
            checkZero = all(item in zero for item in lenSix)
            checkSix = all(item in six for item in lenSix)
            checkNine = all(item in nine for item in lenSix)
            if checkZero is True:
                singleResult.append(0)
            if checkSix is True:
                singleResult.append(6)
            if checkNine is True:
                singleResult.append(9)
    allResults.append(singleResult)
    
    sum = 0
    for i in range(len(allResults)):
        res = "".join(map(str,allResults[i]))
        sum += int(res)
    grandSum += sum



