#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for j in matrix:
        new_list.append(list(map(lambda x: x*x, j)))
    return new_list
