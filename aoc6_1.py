sum = 0
checklist = []
with open('aoc6.txt') as f:
    for line in f:
        if (line == "\n"):
            checklist = []
        line = line.replace('\n','')
        for char in line:
            if char not in checklist:
                checklist.append(char)
                sum +=1

print(sum)
