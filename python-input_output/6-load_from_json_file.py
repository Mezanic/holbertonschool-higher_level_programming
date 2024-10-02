#!/usr/bin/python3
"""This module creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """
     function that creates an Object from a “JSON file”:

    Args:
        filename: file to create an object with
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
