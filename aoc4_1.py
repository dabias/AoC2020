valid = 0
checklist = [False ,False, False, False, False, False, False]
        
with open('aoc4.txt') as f:
    for line in f:
        if (line == "\n"):
            check = 0
            for i in checklist:
                if i:
                    check += 1
            if (check == len(checklist)):
                valid += 1
            checklist = [False ,False, False, False, False, False, False]
        x=line.rstrip().split(" ")
        for string in x:
            if 'byr' in string:
                byr = string.split(":")[1]
                if ((len(byr)==4)&(1920<=int(byr)<=2002)):
                    checklist[0] = True
            elif 'iyr' in string:
                iyr = string.split(":")[1]
                if ((len(iyr)==4)&(2010<=int(iyr)<=2020)):
                    checklist[1] = True
            elif 'eyr' in string:
                eyr = string.split(":")[1]
                if ((len(eyr)==4)&(2020<=int(eyr)<=2030)):
                    checklist[2] = True
            elif 'hgt' in string:
                hgt = string.split(":")[1]
                if ('cm' in hgt):
                    hgtInt = int(hgt.replace('cm',''))
                    if (150<=hgtInt<=193):
                        checklist[3] = True
                if ('in' in hgt):
                    hgtInt = int(hgt.replace('in',''))
                    if (59<=hgtInt<=76):
                        checklist[3] = True
            elif 'hcl' in string:
                hcl = string.split(":")[1]
                hclArray = [char for char in hcl]
                if(hclArray[0]=='#')&(len(hclArray)==7):
                    checklist[4] = True
                    #for i in range(6):
                        #if '\w' not in hclArray[i]:
                        #    checklist[4] = False
            elif 'ecl' in string:
                hclCheck = 0
                hcl = string.split(":")[1]
                if 'amb' in hcl:
                    hclCheck += 1
                if 'blu' in hcl:
                    hclCheck += 1
                if 'brn' in hcl:
                    hclCheck += 1
                if 'gry' in hcl:
                    hclCheck += 1
                if 'grn' in hcl:
                    hclCheck += 1
                if 'hzl' in hcl:
                    hclCheck += 1
                if 'oth' in hcl:
                    hclCheck += 1
                if hclCheck == 1:
                    checklist[5] = True
            elif 'pid' in string:
                pid = string.split(":")[1]
                if len(pid)==9:
                    checklist[6] = True

print(valid)
