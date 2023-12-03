#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = []
    for i in range(len(my_list) - 1, -1, -1):
        my_list2.append(my_list[i])
    for i in my_list2:
        print("{}".format(i))
