largest = 0
with open('aoc5.txt') as f:
    for line in f:
        i= 0
        x = []
        line = line.replace('B','1')
        line = line.replace('R','1')
        line = line.replace('F','0')
        line = line.replace('L','0')
        line = line.replace("\\","")
        line = line.replace('n','')
        x = int(line,2) #convert binary to integer
        if x > largest:
            largest = x

print(largest)
