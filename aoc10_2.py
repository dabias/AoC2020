adapters = [0]
permutations = 1
with open('aoc10.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
adapters.append(adapters[-1]+3)

joltDiff = [None]*(len(adapters)-1)

for i in range(len(adapters)-1):
    joltDiff[i] = adapters[i+1]-adapters[i]

def findPermutations(diffList,index, depth):
    count = 1
    while diffList[index] < 3:
        print('start investigating index: ' + str(index) + ' at depth: ' + str(depth))
        if (diffList[index+1] ) == 1:
            print('permutation found at index: ' + str(index))
            newDiffList = diffList
            newDiffList[index] += newDiffList[index+1]
            del newDiffList[index+1]
            count += findPermutations(newDiffList, index, depth + 1)
    return count

for i in range(len(joltDiff)-1):
    if (i == 0 or ((joltDiff[i-1] == 3 and joltDiff[i] < 3))):
        permutations = permutations*findPermutations(joltDiff, i,0)
print(permutations)
