#!/usr/bin/python3

"""Module define a  class Square"""


class Square:
    """
    Class define Square with private instance attribut

    Attribut :

    size (int) : size of the square

    """


def __init__(self, size=0):
    """
    Initializes a  size of the square.

    Args:
    size (int): size of the square

    Raise:
    TypeError size must be an integer
    ValueError size must be >= 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    self.__size = size
