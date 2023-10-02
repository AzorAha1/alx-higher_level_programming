#!/usr/bin/python3
"""class
comment
"""


class Rectangle:
    """Rectangle
    class called Rectangle
    """
    def __init__(self, __width, __height):
        self.__width = __width
        self.__height = __height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__height + self.__width)
