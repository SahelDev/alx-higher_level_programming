#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list) - 1):
            """print("is {:d} < {:d} ?".format(my_list[i], my_list[i+1]))"""
            if my_list[i] > my_list[i+1]:
                """print("SWITCH")"""
                temp = my_list[i+1]
                my_list[i+1] = my_list[i]
                my_list[i] = temp
                """print("Max : {:d}".format(my_list[i+1]))"""
    return my_list[i+1]
