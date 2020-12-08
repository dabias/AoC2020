baseKey = "shiny gold"

def findChild(key):
    bags = 0
    with open('aoc7.txt') as f:
        for line in f:
            x = line.split("bags contain")
            if (key in x[0]):
                x[1] = x[1].replace('\n','') #sanitize
                x[1] = x[1].replace('.','') #sanitize
                y = x[1].split(",")
                for item in range(len(y)):
                    z = y[item-1].split(' ')
                    #z[0]: space
                    #z[1]: number of bags
                    #z[2] and z[3]: bag descriptor 
                    if z[1] != "no":
                        childSize = findChild(z[2]+ ' ' + z[3])+1
                        #print(z[2]+ ' ' + z[3])
                        #print(childSize)
                        childCount = int(z[1])
                        #print(childCount)
                        bags += childSize*childCount
    return bags
                    
                
bags = findChild(baseKey)
print(bags)
