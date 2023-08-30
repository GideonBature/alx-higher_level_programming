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
        if not isinstance(value, int) or isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ public instance method that
            returns area
        """
        product = (self.__size) * (self.__size)
        return product

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __str__(self):
        """string method for printing with class instance"""
        result = (self.__size) * (self.__size)
        return str(result)
