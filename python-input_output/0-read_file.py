#!/usr/bin/python3
"""Module for read file method"""


def read_file(filename=""):
    """
    Function for read file in UTF8 and print it in stdout

    Args:
        filename: file to read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
