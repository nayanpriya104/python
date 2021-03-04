"""
Rock Paper Scissors
----------------------------
"""


import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')
while(1 < 2):
    print ('\n')
    print ("Rock, Paper, Scissor - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissor")
    if not re.match("[SsRrPp]", userChoice):
        print("Choose a letter:")
        print("[R]ock, [P]aper or [S]cissor")
        continue
    # Echo the user's choice
    print("You choose: {}".format(userChoice))
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print("I chose: {}".format(opponenetChoice))
    if opponenetChoice == str.upper(userChoice):
        print("Tie!")

    elif opponenetChoice == "R" and userChoice == "S":
        print("Scissor beats the Rock, I win!")
        continue
    elif opponenetChoice == "S" and userChoice == "P":
        print("Scissor beats the paper, I win!")
        continue
    elif opponenetChoice == "P" and userChoice == "R":
        print("Paper beats the rock, I win!")
        continue
    else:
        print("You Win!")
