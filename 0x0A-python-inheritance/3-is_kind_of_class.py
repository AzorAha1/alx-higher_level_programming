#!/usr/bin/python3
"""
function
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is the same class or inherited from
    """
    if isinstance(obj, a_class):
        return True
    return False
