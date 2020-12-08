x = []
y = []
done= False

with open('aoc1_1.txt') as f:
    for line in f:
        if (int(line)<1000):
            x.append(int(line))
        else:
            y.append(int(line))

for linex in x:
    if done:
        break
    for liney in y:
        if(linex+liney==2020):
            ans=linex*liney
            done=True
            break

print(ans)
        

    
