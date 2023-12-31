#!/usr/bin/python3
"""
function
"""


def inherits_from(obj, a_class):
    """
    check if obj is an instance of a class that inherits from specified class
    """
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
