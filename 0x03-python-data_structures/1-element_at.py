#!/usr/bin/python3
def element_at(my_list, idx):
    """This function retrieve an element from a list"""
    if idx < 0:
        result = None
    elif idx > len(my_list) - 1:
        result = None
    else:
        result = my_list[idx]
    return result
