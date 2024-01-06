#!/usr/bin/python3
"""this module define a rectangle"""


class Rectangle:
    """this class represent a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This return the value of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method set the value of width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
    
        self.__width = value

    @property
    def height(self):
        """Return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value according some set of condition"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        
        self.__height = value
