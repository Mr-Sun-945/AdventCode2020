'''
Advent Code Day01

Prompt: Check the sum of two nums from a list of num to see which two add up to 2020 and then output the product of the two num
'''

filePath = "D:\Work\Day01_Input.txt"
target_num = 2020

#Function for reading file
def readFile(filePath):
    #Opening file
    num_list = []
    num_inputs = open(filePath, "r")

    #Reading lines into an array
    while num_inputs:
        this_line = num_inputs.readline()
        if this_line == "":
            break
        num_list.append(this_line)
        
    #Return the array
    return num_list

#Function for comparing numbers and getting the end product
def run():
    #Getting info form the file
    num_list = readFile(filePath)
    
    #Comparing the sum of two nums with target num
    for num1 in num_list:
        num1 = int(num1)
        for num2 in num_list:
            num2 = int(num2)
            if num1 != num2 and num1 + num2 == target_num:
                potato = num1*num2
                return potato
    return "lol"

print("The answer is", run())