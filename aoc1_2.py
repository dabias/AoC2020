x =ans = 0
y = []
done= False

with open('aoc1_1.txt') as f:
    for line in f:
        for n in y:
            x = int(line)+n
            if(x==2020):
               ans = int(line)*n
            elif(x<2020):
                for m in y:
                    if(x+int(m)==2020):
                        ans=int(line)*m*n
        y.append(int(line))

print(ans)
        
