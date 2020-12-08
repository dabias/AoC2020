valid = 0
with open('aoc2_1.txt') as f:
    for line in f:
        i = 0
        x=line.rstrip().split(" ")
        occ =x[0].split("-")
        lowerBound = int(occ[0])
        upperBound = int(occ[1])
        letter = x[1].split(":")[0]
        word = x[2]
        for char in word:
            if(char==letter):
                i += 1
        if(lowerBound<=i<=upperBound):
            valid += 1

print(valid)
