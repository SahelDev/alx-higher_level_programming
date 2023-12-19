#!/usr/bin/python3
"""this module defines a class Square with a private instance"""


class Square:
    """this class represent a square with private attribute size"""

    def __init__(self, size):
        """Class constructor"""
        self.__size = size
