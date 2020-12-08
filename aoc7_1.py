baseKey = "shiny gold"
validBags = []

def findParentBags(key):
    with open('aoc7.txt') as f:
        for line in f:
            x = line.split("bags contain")
            if (key in x[1] and x[0] not in validBags):
                validBags.append(x[0])
                #print(validBags)
                #print(x[0])
                findParentBags(x[0])
                #print(validBags)
                
findParentBags(baseKey)
print(len(validBags))
