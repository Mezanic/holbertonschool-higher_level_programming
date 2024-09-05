#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * -1

last_digit = number % 10

ls_d = last_digit

if last_digit == 0:
    print(f"Last digit of {number} is {ls_d} and is 0")

elif last_digit > 5:
    print(f"Last digit of {number} is {ls_d} and is greater than 5")

else:
    print(f"Last digit of {number} is {ls_d} and is less than 6 and not 0")
