#!/usr/bin/python
"""Module contains a function write_file\
        that write a string to a text file and\
        returns the number of character written"""

def write_file(filename="", text=""):
    """definition of func write_file"""
    with open(filename, 'w', encoding="utf-8") as f:
        nc = f.write(text)

    return nc
