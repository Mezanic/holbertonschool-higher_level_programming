#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) <= 0:
        return None

    biggest_number = my_list[0]

    for i in my_list:
        if i > biggest_number:
            biggest_number = i

    return (biggest_number)
