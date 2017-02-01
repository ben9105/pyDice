import math
import random

min = 1
max = 6


dicePlayer1 = raw_input("Player one, do you want to roll?" )
if dicePlayer1 == "yes":
    dice1 = random.randrange(min, max)
    print "Your dice was", dice1
else:
    print "Player two is going to win if you say no."

dicePlayer2 =raw_input("Player two, do you want to roll? ")
if dicePlayer2 == "yes":
    dice2 = random.randrange(min, max)
    print "Your dice was", dice2
else:
    print "That means player one wins"

if dice1 > dice2:
    print "Player one wins!"
elif dice2 > dice1:
    print "Player two wins!"
elif dice1 == dice2:
    print "Tie!"
