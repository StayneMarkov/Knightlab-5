import random

a=""
a = input("Do you want to roll the dice? Press Y or N: ")
if a == 'Y':
    number = random.randint(1,6)
    print (number)
else:
    print ("Okay whateves")
