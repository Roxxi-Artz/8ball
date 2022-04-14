from random import randrange
import random

def Magic8Ball():
    input("What would you like to ask the Magic 8-Ball? ")

    random_number = random.randint(1,9)

    if random_number == 1:
        print("Yes - Definitely.")
    elif random_number == 2:
        print("It is decidedly so.")
    elif random_number == 3:
        print("Without a doubt.")
    elif random_number == 4:
        print("Reply hazy, try again.")
    elif random_number == 5:
        print("Ask again later.")
    elif random_number == 6:
        print("Better not to tell you now.")
    elif random_number == 7:
        print("My sources say no.")
    elif random_number == 8:
        print("Outlook not so good.")
    elif random_number == 9:
        print("Very doubtful.")
    else:
         print("An error has occured, check your code.")
    
    replay()

def replay():
    reply = input("Do you have another question?? [Y/N]  ")
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('what')
        replay()

Magic8Ball()