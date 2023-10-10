#!/usr/bin/python3
"""function
"""


def append_write(filename="", text=""):
    """append_write
    append to a file and returns count
    """
    with open(filename, 'a', encoding="utf-8") as thefile:
        thefile.seek(0)
        thefile.write(text)
        return thefile.tell()
