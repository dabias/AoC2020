sum = 0
firstMember = True
checklist = []

with open('aoc6.txt') as f:
    for line in f:
        if (line == "\n"):
            sum += len(checklist)
            print(len(checklist))
            checklist = []
            firstMember = True
        else:
            line = line.replace('\n','')
            if firstMember:
                for char in line:
                    if char not in checklist:
                        checklist.append(char)
                firstMember = False
            else:
                for char in checklist:
                    if char not in line:
                        checklist.remove(char)

print(checklist)
sum += len(checklist)

print(sum)
