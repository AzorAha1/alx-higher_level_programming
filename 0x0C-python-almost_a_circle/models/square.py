#!/usr/bin/python3
"""class
Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square
    square inherits form Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """str
        str
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size
        size setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update
        update
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to_dictionary
        returns dict rep
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
