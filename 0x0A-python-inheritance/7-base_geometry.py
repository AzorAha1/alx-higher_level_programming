#!/usr/bin/python3
"""
class
"""


class BaseGeometry:
    """BaseGeometry
    empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
