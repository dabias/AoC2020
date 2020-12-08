grid = []
length = 0
trees = 0
with open('aoc3_1.txt') as f:
    for line in f:
        lineInt = []
        for char in line:
            if (char=='#'):
                lineInt.append(1)
            else:
                lineInt.append(0)
        grid.append(lineInt)
        width = len(lineInt)
        length += 1
x = y = 0
while(y<length):
    trees += grid[y][x]
    x = (x + 1) % width
    y += 2

print(trees)
