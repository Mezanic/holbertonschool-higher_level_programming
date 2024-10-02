#!/usr/bin/python3
"""
This module returns the dictionary description with simple data structure for
JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple
    data structure for JSON serialization of an object

    Args:
        obj: obj to return at dict
    """
    return obj.__dict__
