#!/usr/bin/python3
"""Defines a class square"""


class Square:

    """class defines square object"""

    def __init__(self, size=0, position=(0, 0)):

        """__init__ method

        Args:
            size: size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter Function"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instance method that returns area"""

        product = (self.__size) * (self.__size)
        return product

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            result = self.area()
            for i in range(int(result/self.__size)):
                for j in range(self.__position[0]):
                    if self.__position[1] < 0:
                        print(end="")
                    else:
                        print(" ", end="")
                for j in range(int(result/self.__size)):
                    print('#', end="")
                print()
