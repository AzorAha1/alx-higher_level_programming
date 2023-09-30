#!/usr/bin/python3
def add_integer(a, b=98):
    """add
    >>> add_integer(5, 10)
    15
    >>> add_integer(-1, 1)
    0
    >>> add_integer(0, 0):
    0
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
