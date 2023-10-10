#!/usr/bin/python3
"""working on inheritance
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


class Rectangle(BaseGeometry):
    """Rectangle
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator(name="width", value=self.__width)
        super().integer_validator(name="height", value=self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
