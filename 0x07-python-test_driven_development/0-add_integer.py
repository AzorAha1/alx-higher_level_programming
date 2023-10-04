#!/usr/bin/python3
"""function
    this is a function
"""


def add_integer(a, b=98):
    """add
        this function is to add
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 2
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
