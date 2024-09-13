#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Parameters:
    a (int): Integer
    b (int): integer

    Returns:
    int: sum of a and b

    Raises:
    TypeError: if a or b not integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
