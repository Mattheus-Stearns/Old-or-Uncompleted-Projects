import random
import time

whatDice = int(input("\nWelcome to this random dice program. \n\nWould you like to have a random dice, or input your own number?\n\nIf you want a random dice, enter 0.\n\nIf you want to enter your own number, enter 1.\n\n"))

if (whatDice == 0):
    print("\nOk, we will produce a random dice for you in a few moments.\n\n")
    time.sleep(3)
    whatDice = 0
elif (whatDice == 1):
    print("\nOk, we will produce a dice face of your choosing in a few moments.\n")
    time.sleep(3)
    whatDice = 1
else:
    print("\nPlease enter a number between 0 or 1.\n")

randDice = random.randint(1,6)

if (whatDice == 0) and (randDice == 1):
    print('''

    oooooooooooo
    o          o
    o          o
    o    #     o
    o          o
    o          o
    oooooooooooo

    ''')
elif (whatDice == 0) and (randDice == 2):
    print('''

    oooooooooooo
    o          o
    o   #      o
    o          o
    o      #   o
    o          o
    oooooooooooo

    ''')
elif (whatDice == 0) and (randDice == 3):
    print('''

    oooooooooooo
    o          o
    o   #      o
    o       #  o
    o   #      o
    o          o
    oooooooooooo

    ''')
elif (whatDice == 0) and (randDice == 4):
    print('''

    oooooooooooo
    o          o
    o   #  #   o
    o          o
    o   #  #   o
    o          o
    oooooooooooo

    ''')
elif (whatDice == 0) and (randDice == 5):
    print('''

    oooooooooooo
    o          o
    o   #  #   o
    o     #    o
    o   #  #   o
    o          o
    oooooooooooo

    ''')
elif (whatDice == 0) and (randDice == 6):
    print('''

    oooooooooooo
    o          o
    o   #  #   o
    o   #  #   o
    o   #  #   o
    o          o
    oooooooooooo

    ''')
else:
 print("\n")

if (whatDice == 1):
    setDice = int(input("\nPlease input the number that you want to see (from 1 to 6).\n\n"))
    print("\nAnalyzing")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)

    if (setDice == 1):
        print('''

        oooooooooooo
        o          o
        o          o
        o    #     o
        o          o
        o          o
        oooooooooooo

        ''')
    elif (setDice == 2):
        print('''

        oooooooooooo
        o          o
        o   #      o
        o          o
        o      #   o
        o          o
        oooooooooooo

        ''')
    elif (setDice == 3):
        print('''

        oooooooooooo
        o          o
        o   #      o
        o       #  o
        o   #      o
        o          o
        oooooooooooo

        ''')
    elif (setDice == 4):
        print('''

        oooooooooooo
        o          o
        o   #  #   o
        o          o
        o   #  #   o
        o          o
        oooooooooooo

        ''')
    elif (setDice == 5):
        print('''

        oooooooooooo
        o          o
        o   #  #   o
        o     #    o
        o   #  #   o
        o          o
        oooooooooooo

        ''')
    elif (setDice == 6):
        print('''

        oooooooooooo
        o          o
        o   #  #   o
        o   #  #   o
        o   #  #   o
        o          o
        oooooooooooo

        ''')
    else:
        print("\n")
else:
    print("\n")
