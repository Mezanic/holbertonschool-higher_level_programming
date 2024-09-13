#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        quotient = a / b

    except ZeroDivisionError:
        quotient = None

    finally:
        print("Inside result: {}" .format(quotient))
        return quotient


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
