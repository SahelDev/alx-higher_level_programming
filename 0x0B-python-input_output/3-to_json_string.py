#!/usr/bin/python3
"""Module that define func to_json_string"""
import json


def to_json_string(my_obj):
    """Convert serializable `obj` to json string

    Args:
        obj: serializable object

    Returns: string representation of `obj`
    """
    return json.dumps(my_obj)
