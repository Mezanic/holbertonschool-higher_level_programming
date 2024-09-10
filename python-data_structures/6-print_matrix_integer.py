#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for number in row:
            if number == row[0]:
                print("{:d}".format(number), end="")
            else:
                print(" {:d}".format(number), end="")
        print()
