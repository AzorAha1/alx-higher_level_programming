#!/usr/bin/python3
"""class
comment
"""


class Rectangle:
    """Rectangle
    class called Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, __width, __height):
        self.__width = __width
        self.__height = __height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        Rectangle.number_of_instances += 1

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
                string_rep += str(self.print_symbol)
            if i < self.__height - 1:
                string_rep += "\n"
        return string_rep

    def __repr__(self):
        string_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string_rep += self.print_symbol
            if i < self.__height - 1:
                string_rep += "\n"
            return f'Rectangle({self.__width}, {self.__height})'
