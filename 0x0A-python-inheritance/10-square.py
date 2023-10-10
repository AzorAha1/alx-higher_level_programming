#!/usr/bin/python3
"""working on inheritance
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square
    """
    def __init__(self, size):
        self._size = size
        super().__init__(size, size)
