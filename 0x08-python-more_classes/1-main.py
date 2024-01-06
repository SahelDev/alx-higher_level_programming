#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle()

"""my_rectangle = Rectangle(2, 'c')
print(my_rectangle.__dict__)"""

my_rectangle.width = 1
my_rectangle.height = 'a'
print(my_rectangle.__dict__)
