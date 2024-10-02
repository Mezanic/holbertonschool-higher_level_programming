#!/usr/bin/python3
"""This module return JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)

    Args:
        my_obj: obj to return as json
    """
    return json.dumps(my_obj)
