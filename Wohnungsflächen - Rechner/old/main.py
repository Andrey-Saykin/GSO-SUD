shapes = ['Rectangle','Corner','Trapezoid']
roomQuantity = 0

rooms = {}

listStart = "  •"

class Room():
    def __init__(self, name, shape, length, width, slope):
        self.name = name
        self.shape = shape
        self.length = length
        self.width = width
        self.area = 0.0
        self.slope = slope


def askForUnit():
    validAnswers = ["m","cm"]
    print("Which unit do you want to use?:")
    print(f"{listStart} m")
    print(f"{listStart} cm")
    while True:
        answer = input()
        if answer in validAnswers:
            return answer
        else:
            print("Enter only one of the valid options.")

def addRoom(name,shape,length,width,slope,rooms=rooms):
    rooms[name] = {'shape': shape, 'length': length, 'width': width, 'slope': slope}

def askForSlopingRoofAll():
    validAnswers = ["y","n"]
    print("Have one of your rooms sloping roofs? (y/n)")
    while True:
        answer = input()
        if answer in validAnswers:
            return True if answer == validAnswers[0] else False
        else:
            print("Please enter y or n.")

def askForSlopingRoof():
    validAnswers = ["y","n"]
    print("Have this room a sloping roof? (y/n)")
    while True:
        answer = input()
        if answer in validAnswers:
            return True if answer == validAnswers[0] else False
        else:
            print("Please enter y or n.")

def askForRoomQuantity():
    print("How many rooms do you have?")
    while True:
        try: roomQuantity = int(input())
        except ValueError: print("Enter only numbers")
        else:
            if roomQuantity == 0:
                print("Number of rooms should be at least higher than 0")
            elif roomQuantity > 20:
                print("Too many rooms! Valid room number till 20")
            else:
                return roomQuantity

def askForShape():
    validAnswers = ["r","rc","t"]
    print("Which shape has your room?\nIf the shape of your room is:")
    print(f"{listStart} {shapes[0]} - enter {validAnswers[0]}")
    print(f"{listStart} {shapes[1]} - enter {validAnswers[1]}")
    print(f"{listStart} {shapes[2]} - enter {validAnswers[2]}")
    while True:
        answer = input()
        if answer in validAnswers:
            if answer == validAnswers[0]:
                return shapes[0]
            elif answer == validAnswers[1]:
                return shapes[1]
            else:
                return shapes[2]
        else:
            print("Enter only one of the valid options.")

def nameRoom():
    print("Enter a room name. (Remember to take different names)")
    while True:
        name = input()
        if name.strip != "":
            return name
        else:
            print("Name cannot be empty!")

def askForLength():
    print("Enter length of this room")
    while True:
        try: length = int(input())
        except ValueError: print("Length cannto be empty and must be a number")
        else:
            if length == 0:
                print("Length should be at least higher than 0")
            else:
                return length

def askForWidth():
    print("Enter width of this room")
    while True:
        try: width = int(input())
        except ValueError: print("Width cannot be empty and must be a number")
        else:
            if width == 0:
                print("Width should be at least higher than 0")
            else:
                return width

def askForCornerRoom():
    print("In how many rectangles do you want to split your room?")
    try: rectangles = int(input())
    except ValueError: print("Enter only Numbers")
    else:
        if rectangles == 0:
            print("Enter numbers which are higher than 0")
        else:
            for rectangle in range(rectangles):
                rooms[room][rectangle+1] = {'length': askForLength(), 'width': askForWidth()} 

def calculateSurfaces():
    for room in rooms:
        area = int(rooms[room]['length']) * int(rooms[room]['width'])
        rooms[room]['area'] = area
    
def calculateLivingArea():
    area = 0
    for room in rooms:
        area += rooms[room]['area']
    return area

def showAllRooms():
    count = 0
    for room in rooms:
        count+=1
        print(f"\n{count}. {room}:")
        print(f"{listStart}Shape of room: {rooms[room]['shape']}")
        print(f"{listStart}Length and width of room: {rooms[room]['length']}{unit} • {rooms[room]['width']}{unit}")
        print(f"{listStart}Area of room: {rooms[room]['area']}{unit}²")
        if rooms[room]['slope']:
            print(f"{listStart}Has sloping roof")
        

if __name__ == '__main__':

    unit = askForUnit()
    slopingRoofs = askForSlopingRoofAll()
    for room in range(askForRoomQuantity()):
        if slopingRoofs:
            if roomQuantity == 1:
                addRoom(nameRoom(),askForShape(),askForLength(),askForWidth(),True)
            else:
                addRoom(nameRoom(),askForShape(),askForLength(),askForWidth(),askForSlopingRoof())
        else:
            addRoom(nameRoom(),askForShape(),askForLength(),askForWidth(),slopingRoofs)

        calculateSurfaces()

    showAllRooms()
    print(f"\nLiving area: {calculateLivingArea()}{unit}²")
