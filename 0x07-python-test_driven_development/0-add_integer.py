#!/usr/bin/python3
def add_integer(a, b=98):
    """add
    >>> add_integer(1, 2)
    3
    >>> add_integer(100.3, -2)
    98.3
    >>> add_integer(2)
    100
    >>> add_integer(100, -2)
    98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
