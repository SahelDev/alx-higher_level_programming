#!/usr/bin/python3
"""Module that define func that returns an object"""


import json


def from_json_string(str):
    """returns an object
    Args:
        filename (str): file to write to
        text (str): text to write into `filename`
    Returns: number of characters written
    """
    return json.loads(str)
