#!/usr/bin/python3
"""function
"""


def read_file(filename=""):
    """read_file
    reads from filename
    """
    with open(filename, 'r') as thefile:
        print(thefile.read())
