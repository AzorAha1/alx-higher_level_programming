#!/usr/bin/python3
"""class
inherits from class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle
    rectangle class inheriting from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id=id)

    @property
    def width(self):
        """widthgetter
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """widthsetter
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """heightgetter
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """heightsetter
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """xgetter
        this is the x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """xsetter
        this is the x setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ygetter
        this is the y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ysetter
        this is the y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area
        this returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """display
        display function
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str
        str
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """update
        args - non keyword arguments
        kwargs - keyword arguments
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """to_dictionary
        this returns a dictionary representation
        """
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
        }
