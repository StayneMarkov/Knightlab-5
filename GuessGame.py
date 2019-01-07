import random

a = input("Would you like to guess a number?: Reply with Y or N : ")

if a == 'Y' or a == 'y' :
    number = random.randint(1,10)
    guess = input("Guess a number between 1 and 10 : ")
    if type(number)==int:
        if (number==guess):
            print ("Amazing. You are a visionary")
        else:
            print ("Better luck next time . The number was " +str(number))
    else:
        print ("Look at this idiot")
else:
    print ("Okay whateves")
        
