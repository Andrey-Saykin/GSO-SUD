import random

isSchaltjahr = True
schaltjahr = 0 
score = 0

def divide4():
    print("divide4:",schaltjahr/4)
    return True if (schaltjahr/4).is_integer() else False

def divide100():
    print("divide100:",schaltjahr/100)
    return True if (schaltjahr/100).is_integer() else False

def divide400():
    print("divide400:",schaltjahr/400)
    return True if (schaltjahr/400).is_integer() else False

def showScore():
    print(score)

def task1():
    if divide4():
        if divide100():
            if divide400():
                isSchaltjahr = True
            else:
                isSchaltjahr = False
        else: 
            isSchaltjahr = True
    else:
        isSchaltjahr = False
    return isSchaltjahr

def task2():
    isSchaltjahr = divide4()
    isSchaltjahr = divide100()
    isSchaltjahr = divide400()
    return isSchaltjahr

while isSchaltjahr:
    schaltjahr = random.randint(1900,2050)
    #schaltjahr = 1988
    print(schaltjahr)

    isSchaltjahr = task1()
    # isSchaltjahr = task2()

    if isSchaltjahr == True:
        score += 1

showScore()