#!/usr/bin/python3
"""Define if the object is an instance"""


def is_same_class(obj, a_class):
    """ Fonction for check if the object is an instance or not

    Args:
        objs: Object to check
        a_class: class to compare

    Return:
        True if is an instance else false
    """
    if type(obj) is a_class:
        return True

    return False
