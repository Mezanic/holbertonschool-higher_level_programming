#!/usr/bin/python3
"""
Module check if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    function check if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: object to check
        a_class: class to compare

        Return:
            True if the object is an instance or instance subclass else False
    """

    if isinstance(obj, a_class):
        return True

    return False
