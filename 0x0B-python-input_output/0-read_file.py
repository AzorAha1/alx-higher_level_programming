#!/usr/bin/python3
"""function
"""


def read_file(filename=""):
    """read_file
    reads from filenamef
    """
    with open(filename, 'r', encoding="utf-8") as thefile:
        print(thefile.read(), end='')
