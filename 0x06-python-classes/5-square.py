#!/usr/bin/python3
"""Defines a class square"""


class Square:

    """class defines square object"""

    def __init__(self, size=0):

        """__init__ method

        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """Getter Function"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ public instance method that
            returns area
        """
        product = (self.__size) * (self.__size)
        return product

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            result = self.area()
            for i in range(int(result/self.__size)):
                for j in range(int(result/self.__size)):
                    print('#', end="")
                print()
