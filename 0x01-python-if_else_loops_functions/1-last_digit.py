#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if (number < 0):
    lastdigit = number % -10
print("Last digit of {} is ".format(number), end="")
if (lastdigit > 5):
    print("{} and is greater than 5".format(lastdigit))
elif (lastdigit == 0):
    print("{} and is 0".format(lastdigit))
else:
    print("is {} and is less than 6 and not 0".format(lastdigit))
