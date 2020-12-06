'''
Advent Code Day06

Prompt: 
'''

filePath = "D:\Work\AdventCode2020\AdventCode2020\Day06\Day06_Input.txt"

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

def getGroup(input_list):
    
    group_list = []
    group_list.append("")
    num = 0

    #Loop for reading the inputs into arrays of "groups"
    for i in input_list:
        #If did not encounter an empty line
        if i != "\n":
            #Add the current line to the current group in the list
            group_list[num] = (group_list[num] + i)
        else:
            #Move onto the next group
            num += 1
            group_list.append("")
    #Give the list of group back

    return group_list

def countYes(group):
    small_potato = 0
    temp = '#'
    #print(group)
    for i in group:
        #print(i)
        #print('yas')
        if i.isalpha() == True:
            #print('yas')
            for a in temp:
                #print(a, temp[-1])
                #print(a)
                #print('yas')
                #print(a,i, temp[-1])
                if a == i:
                    break
                if a == temp[-1]:
                    small_potato += 1
                    temp = temp + i
                    #print('yas')
                    #print(temp)
                    
    #print(small_potato)
    return small_potato

def run():
    #Getting inputs
    input_list = readFile(filePath)
    potato = 0

    group_list = getGroup(input_list)

    for m in group_list:
        potato += countYes(m)

    print(potato)

run()