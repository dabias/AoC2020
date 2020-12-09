#window is a sliding window of windowLen previous numbers
window = []
windowLen = 25
invalidNum = 0
with open('aoc9.txt') as f:
    for line in f:
        num = int(line)
        valid = False
        if len(window) == windowLen:
            #only true after preamble
            # if the number is the sum of two different numbers in the window, set it as valid
            for i in window:
                for j in window:
                    if (i + j == num) and i != j:
                        valid = True
            if not valid:
                print('first invalid number: ' + line)
                invalidNum = num
                break
        elif len(window) > windowLen:
            print('unexpected window size')
        window.append(num)
        if len(window) > windowLen:
            #remove oldest number
            window.pop(0)
            
with open('aoc9.txt') as f:
    j = 0
    #iterate over potential starts of the contiguous set
    for line in f:
        # if step 1 failed to produce a valid number
        if invalidNum == 0:
            break
        #start the summation with the starting number
        contiSet = [int(line)]
        contiSum = int(line)
        i = 0
        #print('Outer loop: ' + line)
        #add next number to sum until invalid number is either reached or exeeded
        with open('aoc9.txt') as g:
            for innerLine in g:
                if i > j:
                    #this prevents adding preceding numbers or itself to the sum
                    contiSet.append(int(innerLine))
                    contiSum += int(innerLine)
                    #print('Inner loop: ' + line + " " + str(contiSum))
                #if sum exeeds the invalid number, this can not be a valid set
                if contiSum > invalidNum:
                    break
                #if a valid set is found, find smallest and largest member
                elif (contiSum == invalidNum) and (len(contiSet) > 1):
                    contiSet.sort()
                    print(contiSet)
                    #add smallest and largest number of set(first and last item from sorted list)
                    weakness = contiSet[0]+contiSet[-1]
                    print(weakness)
                i += 1

        j += 1
