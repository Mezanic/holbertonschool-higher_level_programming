#!/usr/bin/python3
"""Module for write to a text file method"""


def write_file(filename="", text=""):
    """
    Function for write a string ina  text file in UTF8

    Args:
        filename: file to write in
        text: text to write
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
