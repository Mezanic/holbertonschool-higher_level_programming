#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(number1, 10):
        if number1 != number2 and (number2 + number1) != 17:
            print("{}{}, ".format(number1, number2), end="")
        elif (number2 + number1) == 17:
            print("89")
