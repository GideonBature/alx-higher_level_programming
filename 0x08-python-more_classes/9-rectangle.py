#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle:
    """Defines a class with private instance
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Character # representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_shape = ""
            for _ in range(self.__height):
                rectangle_shape += str(self.print_symbol) * self.__width + '\n'
            return rectangle_shape[:-1]

    def __repr__(self):
        """string representation to recreate new instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message when instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns width == height == size
        """
        return cls(size, size)
