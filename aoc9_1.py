#window is a sliding window of windowLen previous numbers
window = []
windowLen = 25
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
                break
        elif len(window) > windowLen:
            print('unexpected window size')
        window.append(num)
        if len(window) > windowLen:
            #remove oldest number
            window.pop(0)
            
