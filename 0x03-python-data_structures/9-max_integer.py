#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    sorted_nums = sorted(my_list)
    if len(sorted_nums) == 0:
        return None
    return sorted_nums[-1]
