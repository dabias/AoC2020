adapters = []
joltDiff = [0, 0, 0]
diff = 0
joltage = 0
with open('aoc10.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
for adapterJolts in adapters:
    diff = adapterJolts - joltage
    joltDiff[diff-1] += 1
    joltage = adapterJolts

diff = 3
joltDiff[diff-1] += 1
joltage = adapterJolts
print(joltDiff)
ans = joltDiff[0]*joltDiff[2]
print(ans)
