valid = 0
with open('aoc2_1.txt') as f:
    for line in f:
        i = 0
        j = 0
        x=line.rstrip().split(" ")
        occ =x[0].split("-")
        index1 = int(occ[0])
        index2 = int(occ[1])
        letter = x[1].split(":")[0]
        word = [char for char in x[2]]
        if (word[index1-1]==letter):
            j += 1
        if (word[index2-1]==letter):
            j += 1
        if (j==1):
            valid += 1

print(valid)
