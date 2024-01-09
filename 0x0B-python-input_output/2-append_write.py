#!/usr/bin/python3
"""Module with function append_write"""


def append_write(filename="", text=""):
    """func append_write definition"""
    with open(filename, 'a', encoding="utf-8") as f:
        nc = f.write(text)

    return nc
