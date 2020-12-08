largest = 0
with open('aoc5.txt') as f:
    x = []
    for line in f:
        line = line.replace('B','1')
        line = line.replace('R','1')
        line = line.replace('F','0')
        line = line.replace('L','0')
        line = line.replace("\\","")
        line = line.replace('n','')
        x.append(int(line,2)) #convert binary to integer and add to list
    x.sort()
    for i in x:
        if (x[(i-1)+1] != x[i-1]+1):
            print(x[i-1]+1)
