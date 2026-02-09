#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigit = number%10
    if lastdigit > 5:
        print(f"Last digit of {number} is {lastdigit} and is greater than 5")
    elif number%10 == 0:
        print(f"Last digit of {number} is {lastdigit} and is 0")
    else:
        print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
elif number < 0:
    lastdigit = - (abs(number) % 10)
    print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
else:
    print(f"Last digit of 0 is 0 and is 0")
