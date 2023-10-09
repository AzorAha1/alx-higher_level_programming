#!/usr/bin/python3
"""
funtion
"""


def is_same_class(obj, a_class):
    """
    check if object is a particular class
    """
    if isinstance(obj, a_class):
        return True
    elif not isinstance(obj, a_class):
        return False
