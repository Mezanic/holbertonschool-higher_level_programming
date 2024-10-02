#!/usr/bin/python3
"""This module"""

import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file.py').load_from_json_file

file = "add_item.json"


if os.path.exists(file):
    python_list = load_from_json_file(file)

else:
    python_list = []

for arg in sys.argv[1:]:
    python_list.append(arg)

save_to_json_file(python_list, file)
