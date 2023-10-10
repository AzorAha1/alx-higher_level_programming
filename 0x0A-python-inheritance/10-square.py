#!/usr/bin/python3
"""working on inheritance
"""
Rectangle = __import__('9-rectangle.py').Rectangle


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


class Square(Rectangle):
    """Square
    """
    def __init__(self, size):
        self._size = size
        super().__init__(size, size)
