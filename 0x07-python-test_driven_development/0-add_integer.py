#!/usr/bin/python3
"""function
    this is a function
"""


def add_integer(a, b=98):
    """add
        this function is to add
    """
    if (type(a) not in [int, float]) or (a != a or a == float('inf') or a == -float('inf')):
        raise TypeError("a must be an integer")
    elif (type(b) not in [int, float]) or (b != b or b == float('inf') or b == -float('inf')):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
