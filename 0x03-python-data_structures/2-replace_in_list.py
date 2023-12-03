#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        """must returs the original list"""
        result = my_list
    elif idx > len(my_list) - 1:
        """returns the original list"""
        result = my_list
    else:
        my_list[idx] = element
        result = my_list

    return result
