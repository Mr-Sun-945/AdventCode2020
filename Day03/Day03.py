'''
Advent Code Day03

Prompt: Count the amount of # you encounter taking the slope right 3 down 1 through a repeating map
'''

filePath = "D:\Work\Day03_Input.txt"
x = 3
y = 1
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
        
    #Return the array
    return input_list

def run():
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

    for i in input_list:
        #print(i)
        current_line = input_list[y*num]

        #Calculating which space to check
        check_space = (((num*x)+int(char_total))) % int(char_total)

        #print(current_line[check_space])
        current_space = current_line[check_space]

        
        if check_space == (char_total):
            current_space = current_line[0]
        
        ##print("------------")
        ##print("checking line", (y*num))
        ##print("the line is", current_line)
        ##print("checking space", check_space)
        ##print("the space is", current_line[check_space])
        ##print("------------")

        if current_space == tree:
            potato += 1
        num += 1
        #print(num)
        #print(potato)
    #print(char_total)
    print(potato)
    return potato

run()