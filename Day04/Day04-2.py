'''
Advent Code Day04

Prompt: 
'''

filePath = "D:\Work\Day04_Input.txt"

'''byr, iyr, eyr, hgt, hcl, ecl, pid, cid'''

class Passport:
    def __init__(self):
        self.byr = "NULL"
        self.iyr = "NULL"
        self.eyr = "NULL"
        self.hgt = "NULL"
        self.hcl = "NULL"
        self.ecl = "NULL"
        self.pid = "NULL"
        self.cid = "NULL"
    
    def printPassport(self):
        print(self.byr)
        print(self.iyr)
        print(self.eyr)
        print(self.hgt)
        print(self.hcl)
        print(self.ecl)
        print(self.pid)
        print(self.cid)


#Function for reading file
def readFile(filePath):
    #Opening file
    input_list = []
    inputs = open(filePath, "r")

    #Reading lines into an array
    while inputs:
        this_line = inputs.readline()
        #print(this_line)
        if this_line == "":
            break
        input_list.append(this_line)
        
    #Return the array
    return input_list

def getPassport(input_list):
    
    passport_list = []
    passport_list.append("")
    num = 0

    #Loop for reading the inputs into arrays of "passports"
    for i in input_list:
        #If did not encounter an empty line
        if i != "\n":
            #Add the current line to the current passport in the list
            passport_list[num] = (passport_list[num] + i)
        else:
            #Move onto the next passport
            num += 1
            passport_list.append("")
    #Give the list of passport back

    return passport_list

def breakDownPassport(input_str):
    new_input_str = ''
    for i in input_str:
        if i == "\n":
            #print("suh")
            new_input_str += ' '
        else:
            new_input_str += i
    
    #print(new_input_str)

    elements = new_input_str.split(' ')
    #print(elements)

    current_passport = Passport()
    for i in elements:
        #print(i)
        #print(i[:3])
        #print(i[4:])
        if i[:3] == "byr":
            current_passport.byr = i[4:]
        if i[:3] == "iyr":
            current_passport.iyr = i[4:]
        if i[:3] == "eyr":
            current_passport.eyr = i[4:]
        if i[:3] == "hgt":
            current_passport.hgt = i[4:]
        if i[:3] == "hcl":
            current_passport.hcl = i[4:]
        if i[:3] == "ecl":
            current_passport.ecl = i[4:]
        if i[:3] == "pid":
            current_passport.pid = i[4:]
        if i[:3] == "cid":
            current_passport.cid = i[4:]
        
        #current_passport.printPassport()
    return current_passport

def checkPassport(current_passport):
    if current_passport.byr != "NULL" and current_passport.iyr != "NULL" and current_passport.eyr != "NULL" and current_passport.hgt != "NULL" and current_passport.hcl != "NULL" and current_passport.ecl != "NULL" and current_passport.pid != "NULL":
        return True
    else:
        return False

def checkByr(byr):
    #Check if four digit and if are numbers
    total = 0
    for i in byr:
        total += 1
        if i.isdigit() == False:
            return False
    if total != 4:
        return False
    
    #Check if in range
    if int(byr) < 1920 or int(byr) > 2002:
        return False

    return True

def checkIyr(iyr):
    #Check if four digit and if are numbers
    total = 0
    for i in iyr:
        total += 1
        if i.isdigit() == False:
            return False
    if total != 4:
        return False
    
    #Check if in range
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False

    return True

def checkEyr(eyr):
    #Check if four digit and if are numbers
    total = 0
    for i in eyr:
        total += 1
        if i.isdigit() == False:
            return False
    if total != 4:
        return False
    
    #Check if in range
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False
    return True

def checkHgt(hgt):
    if hgt[-2:] == 'cm':
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            return False
    elif hgt[-2:] == 'in':
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            return False
    else:
        return False
        
    return True

def checkHcl(hcl):
    temp = hcl
    if temp[0] != '#':
        return False
    temp = temp[1:]
    total = 0
    for a in temp:
        total += 1
        if a.isdigit() == False and a.isalpha() == False:
            return False
        if a.isalpha() == True:
            if a != 'a' and a != 'b'  and a != 'c'  and a != 'd'  and a != 'e'  and a != 'f':
                return False
    if total != 6:
        return False
    return True

def checkEcl(ecl):
    if ecl != 'amb' and ecl != 'blu' and ecl != 'brn' and ecl != 'gry' and ecl != 'grn' and ecl != 'hzl' and ecl != 'oth':
        return False
    return True

def checkPid(pid):
    total = 0
    for a in pid:
        total += 1
        if a.isdigit() == False:
            return False
    if total != 9:
        return False
    return True

def newCheck(passport):
    if checkPassport(passport) == False:
        return False
    if checkByr(passport.byr) == False:
        return False
    if checkIyr(passport.iyr) == False:
        return False
    if checkEyr(passport.eyr) == False:
        return False
    if checkHgt(passport.hgt) == False:
        return False
    if checkHcl(passport.hcl) == False:
        return False
    if checkEcl(passport.ecl) == False:
        return False
    if checkPid(passport.pid) == False:
        return False

    return True

def run():
    potato = 0
    input_list = readFile(filePath)
    passport_list = getPassport(input_list)

    #print(input_list)

    for i in passport_list:
        #print(i)
        current_passport = breakDownPassport(i)
        #current_passport.printPassport()
        passport_status = newCheck(current_passport)
        if passport_status == True:
            potato += 1
        #print(passport_status)
    
    print(potato)
    return potato


run()

'''
passport01 = Passport()
passport01.byr = "2002"
passport01.iyr = "2012"
passport01.eyr = "2020"
passport01.hgt = "150cm"
passport01.hcl = "#aa3a2a"
passport01.ecl = "grn"
passport01.pid = "087499704"
passport01.cid = "NULL"

#print(checkByr(passport01.byr))
#print(checkIyr(passport01.iyr))
#print(checkEyr(passport01.eyr))
#print(checkHgt(passport01.hgt))
#print(checkHcl(passport01.hcl))
#print(checkEcl(passport01.ecl))
#print(checkPid(passport01.pid))

#print(newCheck(passport01))
'''