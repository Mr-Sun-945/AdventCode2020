'''
Advent Code Day02

Prompt: Check the each line of password and their policy to see how many passwords fit their policy
'''

filePath = "D:\Work\Day02_Input.txt"

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

def checkPassword(pass_line):
    splited_line = pass_line.split(" ")
    #print(splited_line)
    floor_roof = splited_line[0].split("-")

    floor = int(floor_roof[0])
    roof = int(floor_roof[1])
    marker = splited_line[1][0]
    password = splited_line[2]

    marker_num = 0
    for char in password:
        if char == marker:
            marker_num += 1
    
    if marker_num <= roof and marker_num >= floor:
        return True
    else:
        return False


def run():
    potato = 0
    #Getting info form the file
    input_list = readFile(filePath)
    #print(input_list)
    for line in input_list:
        if checkPassword(line) == True:
            potato += 1

    print(potato)

run()