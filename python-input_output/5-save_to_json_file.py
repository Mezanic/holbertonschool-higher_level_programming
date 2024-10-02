#!/usr/bin/python3
"""This module writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    function write an Object to a text file, using a JSON representation

    Args:
        my_obj: obj to write in a text file
        filename: file to write
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dumps(my_obj, f)
