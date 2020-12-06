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

#New counting function
def newCount(group):
    small_potato = 0
    #temp = "".join(set(group[0]))
    #Spliting the lines into different sections
    group = group.splitlines()
    #Setting up the first line as the one to compare to
    temp = group[0]
    #print(group, group[0], '\n--------')
    #print(temp)

    #For each element in the group
    for i in group:
        #If the element is an alpha
        if i.isalpha() == True:
            #For each character in the reference line
            for a in temp:
                #For each character in the current element
                for b in i:
                    #print(b, group[num][-1])
                    #If they are the same
                    if a == b:
                        #Skip this character
                        break
                    #If we reach the end of the element and still have not found a same
                    if b == i[-1]:
                        #Delete the current character in temp
                        temp = temp.replace(a, "")

    #print(temp)
    #Count the characters in temp
    for z in temp:
        small_potato += 1

    #Return result
    return small_potato



def run():
    #Getting inputs
    input_list = readFile(filePath)
    potato = 0
    
    #Spliting up gorups
    group_list = getGroup(input_list)

    for m in group_list:
        #print(m, '\n', '----------')
        potato += newCount(m)

    print(potato)

run()

'''
group0 = ['abc', 'acb', 'ba']
print(newCount(group0))
'''