#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != {} and a_dictionary is not None:
        lists = []
        for i in a_dictionary:
            lists.append(a_dictionary[i])
        maximun = max(lists)
        for i in a_dictionary:
            if a_dictionary[i] == maximun:
                return i
