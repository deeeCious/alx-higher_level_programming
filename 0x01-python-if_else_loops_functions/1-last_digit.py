#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extracting the last digit of the number
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
# Check if last digit is greater than 5
if last_digit > 5:
    print("Last digit of {number} and is greater than 5")
elif last_digit == 0:
    print("Last digit of {number} and is 0")
else:
    print("Last digit of {number} and is less than 6 and not 0")
