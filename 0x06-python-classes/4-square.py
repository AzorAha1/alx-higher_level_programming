#!/usr/bin/python3
"""class
comment
"""


class Square:
    """square
    comment
    """
    def __init__(self, __size):
        self.__size = __size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
