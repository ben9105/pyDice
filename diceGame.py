import math
import random

min = 1
max = 6

dice = raw_input("Are you ready to roll the dice? ")
if dice == "yes":
    print random.randrange(min, max)
elif dice == "y":
    print random.randrange(min, max)
else:
    print "Are you sure you don't want to roll?"
