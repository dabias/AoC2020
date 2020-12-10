adapters = [0]
permutations = 1
with open('aoc10.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
adapters.append(adapters[-1] + 3)

joltDiff = [None]*(len(adapters)-1)

for i in range(len(adapters)-1):
    joltDiff[i] = adapters[i+1]-adapters[i]

def findPermutations(diffList, index):
    count = 0
    if diffList[index + 1] < 3:
        count += findPermutations(diffList, index + 1)
        if (diffList[index] + diffList[index + 1]) <= 3:
            print('permutations found at index: ' + str(index))
            newDiffList = []
            for item in diffList:
                newDiffList.append(item)
            newDiffList[index] += newDiffList[index + 1]
            del newDiffList[index+1]
            count += findPermutations(newDiffList, index)
        return count
    else:
        return 1

firstIteration = True
preceding3 = False
for i in range(len(joltDiff)-1):
    if firstIteration or (preceding3 and joltDiff[i] < 3):
        print('starting point found at index: ' + str(i))
        permutations = permutations*findPermutations(joltDiff, i)
    print(preceding3)
    firstIteration = False
    if joltDiff[i] == 3:
        preceding3 = True
    else:
        preceding3 = False
print(permutations)


