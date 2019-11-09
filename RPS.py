#!/usr/bin/env python3

import random as rand

def compThrow():
    compThrow.x = rand.randint(1,3)
    if compThrow.x == 1:
        print("computer throws rock")
    elif compThrow.x == 2:
        print("computer throws scissors")
    elif compThrow.x == 3:
        print("computer throws paper")

compThrow()

def yourThrow():
    yourThrow.yourChoice = input("What do you choose? Type rock, paper, or scissors.")

yourThrow()

def whoWins():
    # print(compThrow.x)
    print(yourThrow.yourChoice)
    if compThrow.x == 1 and yourThrow.yourChoice == str("rock"):
        print("Both rock. Tie")
    elif compThrow.x == 2 and yourThrow.yourChoice == str("scissors"):
        print("Both scissors. Tie")
    elif compThrow.x == 3 and yourThrow.yourChoice == str("paper"):
        print("Both scissors. Tie")
    elif compThrow.x == 1 and yourThrow.yourChoice == str("paper") 
        or compThrow.x == 3 and yourThrow.yourChoice == str("paper"):
        print("You win. You chose " + yourThrow.yourChoice + "and it chose rock.")
    # elif compThrow.x == 3 and yourThrow.yourChoice == str("paper"):
    #     print("Both scissors. Tie")
    # elif compThrow.x == 3 and yourThrow.yourChoice == str("paper"):
    #     print("Both scissors. Tie")
whoWins()
