'''
Advent Code Day03

Prompt: Count the amount of # you encounter taking the slope right 3 down 1 through a repeating map
'''

filePath = "D:\Work\Day03_Input.txt"
x1 = 1
y1 = 1
x2 = 3
y2 = 1
x3 = 5
y3 = 1
x4 = 7
y4 = 1
x5 = 1
y5 = 2
tree = "#"

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
        
    inputs.close()
    #Return the array
    return input_list

#Function for getting the total amount of lines
def getLineTotal(input_list):
    line_total = 0
    for i in input_list:
        line_total += 1
    return line_total

#Function for checking how many trees are in a file
def checkTree(x, y):
    #Getting inputs
    input_list = readFile(filePath)
    #Counting the amount of char in a line
    char_total = -1
    for i in input_list[0]:
        char_total += 1
    #print(char_total)
    
    #Iterating through the map
    num = 0
    potato = 0

    line_total = getLineTotal(input_list)

    for i in input_list:
        #print(i)

        #Checking if the next line is out of bounds
        if y*num > line_total:
            break
        current_line = input_list[y*num]

        #Finding out which space to check
        #Calculating which space to check
        check_space = (((num*x)+int(char_total))) % int(char_total)

        #Getting the char in the check_space
        #print(current_line[check_space])
        current_space = current_line[check_space]

        '''
        ##print("------------")
        ##print("checking line", (y*num))
        ##print("the line is", current_line)
        ##print("checking space", check_space)
        ##print("the space is", current_line[check_space])
        ##print("------------")
        '''

        if current_space == tree:
            potato += 1
        num += 1
        #print(num)
        #print(potato)
    #print(char_total)
    print(potato)
    return potato

def run():
    big_potato = 1

    #Checking all the slopes
    potato0 = checkTree(x1, y1)
    potato1 = checkTree(x2, y2)
    potato2 = checkTree(x3, y3)
    potato3 = checkTree(x4, y4)
    potato4 = checkTree(x5, y5)

    #Getting the final answer
    big_potato *= potato0
    big_potato *= potato1
    big_potato *= potato2
    big_potato *= potato3
    big_potato *= potato4
    print(big_potato)

run()