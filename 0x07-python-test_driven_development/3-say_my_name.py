#!/usr/bin/python3
"""function to print name
    prints name
"""


def say_my_name(first_name="empty", last_name=""):
    """say_my_name
        this function prints first name and last
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))