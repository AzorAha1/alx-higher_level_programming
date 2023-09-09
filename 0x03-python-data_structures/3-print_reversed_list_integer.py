#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        if i not in my_list:
            return None
        print("{:d}".format(my_list))