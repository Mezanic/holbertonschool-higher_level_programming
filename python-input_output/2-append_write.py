#!/usr/bin/python3
"""Module for append text in a file method"""


def append_write(filename="", text=""):
    """
    Function for apend text in file (utf-8)

    Args:
        filename: file to append
        text: will be append
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
