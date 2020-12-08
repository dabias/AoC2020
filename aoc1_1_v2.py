x =ans = 0
y = []
done= False

with open('aoc1_1.txt') as f:
    for line in f:
        for n in y:
            if(int(line)+n==2020):
               ans = int(line)*n
        y.append(int(line))

print(ans)
        
