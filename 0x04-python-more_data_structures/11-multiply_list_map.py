#!/usr/bin/python3
def multiply_list_map(mylist=[], number=0):
    return list(map(lambda row: [x * number for x in row], filter(lambda n: isinstance(n, list), mylist)))