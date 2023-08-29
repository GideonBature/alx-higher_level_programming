#!/usr/bin/python3
"""Defines a class square"""


class Square:

    """class defines square object"""

    def __init__(self, size=0):

        """__init__ method

        Args:
            size: size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ public instance method that
            returns area
        """
        product = (self.__size) * (self.__size)
        return product
