#script for Aoc 8.1 and 8.2
#by Douwe Brinkhorst
acc = 0
pc = 0
pcList = []
instrList = []
#one nop/jmp instr must be replaced with jmp/nop
#the jth occurence of jmp/nop must be replaced
#i iterates over jmp/nop occurences
i = j = 0

with open("AoC8.txt") as f:
    for line in f:
        instr = line.replace("\n","")
        instrList.append(instr)

while(1):
    instr = instrList[pc]
    opcode = instr.split(" ")[0]
    arg = int(instr.split(" ")[1])
    #print(str(pc) + ' ' + opcode + ' ' + str(arg) + ' acc = ' + str(acc))
    if pc in pcList:
        #previously executed instruction (loop) found
        #reset program state
        acc = 0
        pc = 0
        pcList = []
        i = 0
        #attempt replacing next jmp/nop occurence
        j += 1
        continue
    else:
        pcList.append(pc)
    if opcode == 'acc':
        acc += arg
        pc += 1
    elif opcode == 'jmp':
        if i == j:
            #execute nop isntead of jmp
            pc += 1
        else:
            pc += arg
        i += 1
    elif opcode == 'nop':
        if i == j:
            #execute jmp isntead of nop
            pc += arg
        else:
            pc += 1
        i += 1
    else:
        print('unexpected opcode')
    if pc >= len(instrList): 
        print('end of program reached, exiting...')
        print(acc)
        break


