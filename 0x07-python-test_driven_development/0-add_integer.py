#!/usr/bin/python
"""This module contains math function add , to add
        integers
   The function add convert output into integer .
   It also thrown exceptions with Non Number Value
   Usage of the function is obvious"""
        


def add_integer(a, b=98):
    """Definition of function add_integer 
            it's take two integers or float as input then
            output their sum"""

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
