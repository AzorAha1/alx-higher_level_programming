#!/usr/bin/python3
"""function
    this is a function
"""


def add_integer(a=10, b=98):
    """add
        this function is to add
    """
    if type(a) not in [int, float] or a == float('inf') or a != a:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float] or b == float('inf') or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
