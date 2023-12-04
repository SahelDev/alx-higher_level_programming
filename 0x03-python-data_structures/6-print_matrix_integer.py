#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        for i in range(len(j)):
            print("{}".format(j[i]), end="" if i == len(j) - 1 else " ")

        print()
