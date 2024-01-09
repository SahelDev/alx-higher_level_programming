#!/usr/bin/python
"""Module contains a function write_file\
        that write a string to a text file and\
        returns the number of character written"""


def write_file(filename="", text=""):
     """Write `text` to `filename`

    Args:
        filename (str): file to write to
        text (str): text to write into `filename`

    Returns: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
