'''
Advent Code Day05

Prompt: 
'''

filePath = "D:\Work\AdventCode2020\AdventCode2020\Day05\Day05_Input.txt"

class Seat:
    def __init__(self):
        self.row = None
        self.clm = None
        self.ID = None
    def getSeatID(self):
        seat_ID = (self.row*8+self.clm)
        self.ID = seat_ID
        return seat_ID
    def printSeat(self):
        print('Row:', self.row, 'Column:', self.clm, 'ID', self.ID)

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

def getRow(boarding_pass):
    row_info = boarding_pass[:7]
    small_potato = 0
    power_num = pow(2, 7)
    #print(power_num)
    num = 0
    for i in row_info:
        if i == 'F':
            small_potato += 0
        if i == 'B':
            small_potato += (power_num/pow(2, num+1))
            #print(num)
            #print(power_num/pow(2, num+1))
        num+=1
    return small_potato

def getClm(boarding_pass):
    clm_info = boarding_pass[7:]
    #print(clm_info)
    small_potato = 0
    power_num = pow(2, 3)
    #print(power_num)
    num = 0
    for i in clm_info:
        if i == 'L':
            small_potato += 0
        if i == 'R':
            small_potato += (power_num/pow(2, num+1))
            #print(pow(2, num+1))
            #print(power_num/pow(2, num+1))
        num+=1
    return small_potato

def run():
    #Getting inputs
    input_list = readFile(filePath)
    seat_list = []
    potato = 0

    for i in input_list:
        new_seat = Seat()
        new_seat.row = getRow(i)
        new_seat.clm = getClm(i)
        new_seat.getSeatID()
        #new_seat.printSeat()
        seat_list.append(new_seat)
        
        if new_seat.ID > potato:
            potato = new_seat.ID

    print(potato)
    return potato

run()

'''
bp = 'FBFBBFFRLR'

#print(getRow(bp))
print(getClm(bp))
'''