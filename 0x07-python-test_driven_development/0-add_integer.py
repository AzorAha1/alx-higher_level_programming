#!/usr/bin/python3
"""function
    this is a function
"""


def add_integer(a, b=98):
    """add
        this function is to add
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
