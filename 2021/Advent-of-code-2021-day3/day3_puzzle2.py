#finding oxygen_generator_rating
lines = []
with open('input.txt') as f:
    lines = f.readlines()
    
f.close()    

for j in range(0,12):
    zeros = 0
    ones = 0
    for i in range(len(lines)):
        if(int(lines[i][j]) == 0):
            zeros += 1
        else:
            ones += 1
    
    if(zeros > ones): 
        i = 0             
        while(i < len(lines)):
            if(int(lines[i][j]) == 1):
                  line = lines[i]
                  lines.remove(line)
                  i = 0
            else:
                i += 1

    else:
        i = 0             
        while(i < len(lines)):
            if(int(lines[i][j]) == 0):
                  line = lines[i]
                  lines.remove(line)
                  i = 0
            else:
                i += 1

oxygen_generator_rating = int(lines[0],2)

#finding CO2 scrubber rating
lines = []
with open('input.txt') as f:
    lines = f.readlines()
    
f.close()    

for j in range(0,12):
    zeros = 0
    ones = 0
    for i in range(len(lines)):
        if(int(lines[i][j]) == 0):
            zeros += 1
        else:
            ones += 1
    
    if(zeros <= ones ): 
        i = 0             
        while(i < len(lines)):
            if(int(lines[i][j]) == 1):
                  line = lines[i]
                  lines.remove(line)
                  i = 0
            else:
                i += 1

    else:
        i = 0             
        while(i < len(lines)):
            if(int(lines[i][j]) == 0):
                  line = lines[i]
                  lines.remove(line)
                  i = 0
            else:
                i += 1
                
CO2_scrubber_rating = int(line,2)

print(CO2_scrubber_rating * oxygen_generator_rating)


