#!/usr/bin/python3
"""
Module check if the object  is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Function check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: object to check
        a_class: class to compare

    Return:
        True if the is an instance of a class that inherited from specified
        class else False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    return False
