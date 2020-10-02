"""
Author: Bryson Rogers
A dice simulator that will select up to 
five random numbers between 1 and 6
"""
# All the dice have at least one different formula
# so none of the dice should get the same number for 
#same reason

# Die one is just the first time measurment in 
# seconds modulo 6 and add 1
def dieOne(sec):
    return (sec % 6 + 1)

def dieTwo(mnts, sec, s):
    if ((s % 2 == 1)):
        num = 60 - sec
    else:
        num = mnts
    return (num % 6 + 1)

def dieThree(mnts, sec, s):
    if ((sec % 2 == 1)):
        num = 60 - s
    else:
        num = 60 - mnts
    return (num % 6 + 1)

def dieFour(mnts, sec, s):
    if ((mnts % 2 == 1)):
        num = (mnts + sec)
    else:
        num = (mnts + s)
    return (num % 6 + 1)

def dieFive(mnts, sec, s):
        num = (mnts + sec + s)
        return (num % 6 + 1)

def main():
    from datetime import datetime
    rollAgain = "y"
    while (rollAgain != "n"):
        # time stamp one when the loop begins. 
        # Minute and seconds.
        timeOne = datetime.now()
        mnts = int(timeOne.strftime("%M"))
        sec = int(timeOne.strftime("%S"))
        # input for number of Dice.
        cubes = int(input("How many dice would you like to roll? (1-5): "))
        # time stamp two when the user enters  the first input
        # in the loop. It's just seconds because minutes was not 
        #likely to have changed.
        timeTwo = datetime.now()
        s = int(timeTwo.strftime("%S"))
        
        if (cubes == 1):
            dOne = dieOne(sec)
            
            print ("Die one : ", dOne)

        elif (cubes == 2):
            dOne = dieOne(sec)
            dTwo = dieTwo(mnts, sec, s)
            
            print ("Die one : ", dOne)
            print ("Die two : ", dTwo)

        elif (cubes == 3):
            dOne = dieOne(sec)
            dTwo = dieTwo(mnts, sec, s)
            dThree = dieThree(mnts, sec, s)
            
            print ("Die one : ", dOne)
            print ("Die two : ", dTwo)
            print ("Die three : ", dThree)

        elif (cubes == 4):
            dOne = dieOne(sec)
            dTwo = dieTwo(mnts, sec, s)
            dThree = dieThree(mnts, sec, s)
            dFour = dieFour(mnts, sec, s)
            
            print ("Die one : ", dOne)
            print ("Die two : ", dTwo)
            print ("Die three : ", dThree)
            print ("Die four : ", dFour)

        elif (cubes == 5):
            dOne = dieOne(sec)
            dTwo = dieTwo(mnts, sec, s)
            dThree = dieThree(mnts, sec, s)
            dFour = dieFour(mnts, sec, s)
            dFive = dieFive(mnts, sec, s)
            
            print ("Die one : ", dOne)
            print ("Die two : ", dTwo)
            print ("Die three : ", dThree)
            print ("Die four : ", dFour)
            print ("Die five : ", dFive)
        # A little error handling
        else:
            print("Sorry we only have 5 dice.")
        # Exit loop?
        rollAgain = input("Would you like to roll again? (y/n): ")

if __name__ == "__main__":
    main()