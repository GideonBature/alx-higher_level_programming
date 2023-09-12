#!/usr/bin/python3
"""a class with instance method
"""


class BaseGeometry:
    """a base class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle - child of BaseGeometry
    """
    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns print() and str() representation of
        a rectangle
        """
        string = f"[Rectangle] {self.__width}/{self.__height}"
        return string


class Square(Rectangle):
    """A square - child of Rectangle
    """
    def __init__(self, size):
        """Initializes a new square

        Args:
            size (int): length of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of square
        """
        return super().area()

    def __str__(self):
        """Returns the print() and str() representation
        of a square
        """
        string = f"[Square] {self.__size}/{self.__size}"
        return string
