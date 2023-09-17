#!/usr/bin/python3
"""Rectangle Class that inherits from Base
"""
from base import Base


class Rectangle(Base):
    """Rectangle class with private instances
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        space = " "
        newline = "\n"
        if self.__y == 0:
            pass
        else:
            print(newline * (self.__y - 1))
        for i in range(self.__height):
            print(space * self.__x, end="")
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        str1 = "[Rectangle]"
        str2 = f"({self.id})"
        str3 = f"{self.__x}/{self.__y}"
        str4 = f"{self.__width}/{self.__height}"
        return str1 + " " + str2 + " " + str3 + " - " + str4

    def update(self, *args, **kwargs):
        n_args = len(args)
        if n_args >= 1:
            self.id = args[0]
        if n_args >= 2:
            self.__width = args[1]
        if n_args >= 3:
            self.__height = args[2]
        if n_args >= 4:
            self.__x = args[3]
        if n_args >= 5:
            self.__y = args[4]

        for k, v in kwargs.items():
            if k == 'id':
                self.id = v
            if k == 'width':
                self.__width = v
            if k == 'height':
                self.__height = v
            if k == 'x':
                self.__x = v
            if k == 'y':
                self.__y = v

    def to_dictionary(self):
        return ({
                    'x': self.__x,
                    'y': self.__y,
                    'id': self.id,
                    'height': self.__height,
                    'width': self.__width
                })
