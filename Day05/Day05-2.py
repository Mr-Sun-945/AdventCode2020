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
    seat_availability = [[False for x in range(2)] for y in range(1023)]
    
    large = 0
    little = 1000000

    #Running through the input
    for i in input_list:
        new_seat = Seat()
        new_seat.row = getRow(i)
        new_seat.clm = getClm(i)
        new_seat.getSeatID()
        #new_seat.printSeat()
        #seat_list.append(new_seat)
        
        #Addeding the seat to the list and marking it True to say that it's taken
        seat_availability[int(new_seat.ID)][0] = new_seat
        seat_availability[int(new_seat.ID)][1] = True

        #Getting the biggest and smallest ID
        if new_seat.ID > large:
            large = new_seat.ID
        if new_seat.ID < little:
            little = new_seat.ID
        
    
    #Deleting the empty elements in the array
    for m in range(int(little)):
        seat_availability.pop(0)
    for n in range(1023 - int(large)):
        seat_availability.pop()

    potato = Seat()

    #Checking for the one in the list that is not True
    num = 0
    for i in seat_availability:
        #print(i[0])
        if i[1] != True:
            potato = int(seat_availability[num-1][0].ID) + 1
        num += 1

    print(potato)

    #print(seat_availability)
    #large_seat.printSeat()
    #little_seat.printSeat()
        
    


run()

'''
bp = 'BBBBBBBRRR'

print(getRow(bp))
print(getClm(bp))

w = 1
h = 4
twoD = [[0 for x in range(w)] for y in range(h)]
print(twoD)
'''
