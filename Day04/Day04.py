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

def run():
    potato = 0
    input_list = readFile(filePath)
    passport_list = getPassport(input_list)

    #print(input_list)

    for i in passport_list:
        #print(i)
        current_passport = breakDownPassport(i)
        #current_passport.printPassport()
        passport_status = checkPassport(current_passport)
        if passport_status == True:
            potato += 1
    
    print(potato)
    return potato


run()