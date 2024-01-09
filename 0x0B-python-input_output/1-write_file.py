#!/usr/bin/python
"""Module contains a function write_file\
        that write a string to a text file and\
        returns the number of character written"""


def write_file(filename="", text=""):
    """definition of func write_file"""
    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)