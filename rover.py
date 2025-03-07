
#maximum x and y axis 
maxX = 0
maxY = 0
outBounds = False 

# x, y and direction
roverPosX = 0
roverPosY = 0
roverDirection = ''
coordList = ''

def checkInputContainsNumbers(pos,numberOfCharsToCheck):
    global coordList

    coordList = pos.split(' ')
    count=1
    for i in coordList:
        if i.isdigit() == False:
            print("Invalid input")
            exit()
        if count == numberOfCharsToCheck: 
            break
        count+=1

#gets numbers
def updatePlateauBounds(pos):
    global maxX,maxY
    
    maxX = coordList.pop(0)
    maxY = coordList.pop(0)

    maxX = int(maxX)
    maxY = int(maxY)

def checkOutOfBounds(x,y):
   global outBounds, maxX, maxY
    #checking rover bounds
   if x > maxX:
        outBounds = True
        print("Rover out of bounds")
   elif y > maxY:
        outBounds = True
        print("Rover out of bounds")

       
#gets numbers
def updateRoverPosition(pos):
    global roverPosX,roverPosY,roverDirection
    
    coordList = pos.split(' ')

    roverPosX = coordList.pop(0)
    roverPosY = coordList.pop(0)
    roverDirection = coordList.pop(0)

    roverPosX = int(roverPosX)
    roverPosY = int(roverPosY)
    roverDirection = roverDirection


def checkValidDirection(direction):

    match direction:
        case "N":
            pass
        case "S":
            pass
        case "E":
            pass
        case "W":
            pass
        case _:
            print("You did not enter N E S W")
            exit()


def roverMovement(movement, direction):
    global roverPosX, roverPosY, i
    #changing direction of rover based on entered movement/rotation
    

    for i in movement:

        if i == "L":
            #north
            match direction:
                case "N":
                    direction = "W"
                case "S":
                    direction = "E"
                case "E": 
                    direction = "N"
                case "W":
                    direction = "S"

        elif i == "R":
            #north
            match direction:
                case "N":
                    direction = "E"
                case "S":
                    direction = "W"
                case "E": 
                    direction = "S"
                case "W":
                    direction = "N"

        elif i == "M":
            # add movement

            match direction:
                case "N":
                    roverPosY += 1
                case "S":
                    roverPosY -= 1
                case "E":
                    roverPosX += 1  
                case "W":
                    roverPosX -= 1
        
            
        else:
            print("You did not enter L R or M")
            exit()


#bounds input
plateauBounds = input("Please enter plateau right coordinates, e.g, 5 5: ")

while outBounds == False:

    checkInputContainsNumbers(plateauBounds, 2)
    updatePlateauBounds(plateauBounds)
    
    # ROVER ONE #

    #next move pos input
    roverStartPoint = input("Please enter rover one start point, e.g, 2 0 N: ")
    
    checkInputContainsNumbers(roverStartPoint,2)
    #get values
    updateRoverPosition(roverStartPoint)

    #check rover in bounds
    checkOutOfBounds(roverPosX,roverPosY)
    if outBounds == True:
        break
    
    #check direction is NESW
    checkValidDirection(roverDirection)

    roverMovementInput =  input("Please enter one rover movement, e.g, RMLM: ")

    roverMovement(roverMovementInput, roverDirection)

    print("Rover one new location: ", roverPosX, roverPosY, roverDirection)

    # ROVER TWO #
      
    #next move pos input
    roverStartPoint = input("Please enter rover two start point, e.g, 2 0 N: ")
    
    #get values
    updateRoverPosition(roverStartPoint)

    #check rover in bounds
    checkOutOfBounds(roverPosX,roverPosY)
    if outBounds == True:
        break
    
    #check direction is NESW
    checkValidDirection(roverDirection)

    roverMovementInput =  input("Please enter two rover movement, e.g, RMLM: ")

    roverMovement(roverMovementInput, roverDirection)

    print("Rover two new location: ", roverPosX, roverPosY, roverDirection)
            
    break


