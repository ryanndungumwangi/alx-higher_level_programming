#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Check if a number is +ve, -ve or zero
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
