#!/usr/bin/python3
"""working on inheritance
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square
    """
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
