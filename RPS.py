#!/usr/bin/env python3

import random as rand

win = 0
loss = 0
tie = 0
def compThrow():
    compThrow.x = rand.randint(1,3)
    if compThrow.x == 1:
        compThrow.x = "rock"
        # print("computer throws rock")
    elif compThrow.x == 2:
        compThrow.x = "scissors"
        # print("computer throws scissors")
    elif compThrow.x == 3:
        compThrow.x = "paper"
        # print("computer throws paper")
compThrow()

def yourThrow():
    yourThrow.yourChoice = input("What do you choose? Type rock, paper, or scissors.")
yourThrow()

def playAgain():
    compThrow()
    yourThrow()
    whoWins()

def whoWins():
    global tie
    global win
    global loss
    if compThrow.x == yourThrow.yourChoice:
        tie += 1
        print("Both chose " + compThrow.x + ". Tie! Wins: " + str(win) + " Losses: " + str(loss) + " Ties: " + str(tie))
        print("New game.")
        playAgain()
    elif compThrow.x == "rock" and yourThrow.yourChoice == str("paper") or compThrow.x == "paper" and yourThrow.yourChoice == str("scissors") or compThrow.x == "scissors" and yourThrow.yourChoice == str("rock"):
        win +=1
        print("You chose " + yourThrow.yourChoice + " and it chose " + compThrow.x + ". Victory! Wins: " + str(win) + " Losses: " + str(loss) + " Ties: " + str(tie))
        print("New game.")
        playAgain()
    elif compThrow.x == "rock" and yourThrow.yourChoice == str("scissors") or compThrow.x == "paper" and yourThrow.yourChoice == str("rock") or compThrow.x == "scissors" and yourThrow.yourChoice == str("paper"):
        loss +=1
        print("You chose " + yourThrow.yourChoice + " and it chose " + compThrow.x + ". Defeat! Wins: " + str(win) + " Losses: " + str(loss) + " Ties: " + str(tie))
        print("New game.")
        playAgain()
whoWins()
