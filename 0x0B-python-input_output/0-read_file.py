#!/usr/bin/python3
"""function
"""


def read_file(filename=""):
    """read_file
    reads from filename
    """
    with open(filename, 'r', encoding='utf-8') as thefile:
        my_file = thefile.read()
    print(my_file)
