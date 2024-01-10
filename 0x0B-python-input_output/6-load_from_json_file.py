#!/usr/bin/python3
"""Module define function that creates an object from a file"""

import json

def load_from_json_file(filename):
    """
    define load_from_json_file func\
            args: filename
            """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
