#!/usr/bin/python3
"""This module return object represented by a JSON string:"""
import json


def from_json_string(my_str):
    """
    function return an object represented by a JSON string:

    Args:
        my_str: obj to return as JSON string
    """
    return json.loads(my_str)
