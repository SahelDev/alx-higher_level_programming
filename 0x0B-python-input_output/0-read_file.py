#!/usr/bin/python3
"""Module defining read a file function"""


def read_file(filename=""):
    """read function definition"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
