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
    input("What do you choose? Type rock, paper, or scissors.")

yourThrow()

def whoWins():
    if compThrow.x == 1 and yourThrow.input == str("rock")
        print("Both rock. Tie")
whoWins()
