#!/usr/bin/python3
"""function
"""


def write_file(filename="", text=""):
    """write_file
    writes to a file and returns count
    """
    with open(filename, 'w', encoding="utf-8") as thefile:
        thefile.write(text)
        return thefile.tell()
