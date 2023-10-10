#!/usr/bin/python3
"""function
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as thefile:
        thefile.write(text)
        return thefile.tell()
