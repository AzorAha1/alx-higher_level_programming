#!/usr/bin/python3
"""function
    this is a function to print a square
"""


def print_square(size=3):
    """print_square
        this is a function that that print square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
