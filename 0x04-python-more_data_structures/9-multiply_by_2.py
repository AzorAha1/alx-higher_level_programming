#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    for keys, values in a_dictionary.items():
        newdic[keys] = values * 2
    return newdic
