#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    if idx < 0:
        """must returns copy of the original list"""
        result = new_list
    elif idx > len(my_list) - 1:
        """returns a copy of the original list"""
        result = new_list
    else:
        new_list[idx] = element
        result = new_list
    return result
