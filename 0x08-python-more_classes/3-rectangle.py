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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string_rep+="#"
            if i < self.__height - 1:
                string_rep += "\n"
        return string_rep