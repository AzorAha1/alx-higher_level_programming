#!/usr/bin/python3
"""working on inheritance
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator(name="width", value=width)
        super().integer_validator(name="height", value=height)
