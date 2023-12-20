#!/usr/bin/python3
"""this module defines a class Square with a private instance"""


class Square:
    """this class represent a square with private attribute size"""

    def __init__(self, size=0):
        """Class constructor"""
        self.__size = size

    def area(self):
        """Function that return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """function that print the square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
