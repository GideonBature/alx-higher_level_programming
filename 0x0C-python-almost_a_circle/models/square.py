#!/usr/bin/python3
"""Square Class that inherits from Rectangle
"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class with private instances
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        str1 = "[Square]"
        str2 = f"({self.id})"
        str3 = f"{self.__x}/{self.__y}"
        str4 = f"{self.__size}"
        return str1 + " " + str2 + " " + str3 + " - " + str4

    def update(self, *args, **kwargs):
        n_args = len(args)
        if n_args >= 1:
            self.id = args[0]
        if n_args >= 2:
            self.__size = args[1]
        if n_args >= 3:
            self.__x = args[2]
        if n_args >= 4:
            self.__y = args[3]

        for k, v in kwargs.items():
            if k == 'id':
                self.id = v
            if k == 'size':
                self.__size = v
            if k == 'x':
                self.__x = v
            if k == 'y':
                self.__y = v
