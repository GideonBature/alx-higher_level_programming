#!/usr/bin/python3
"""Rectangle Class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class with private instances
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        Base.__init__(self, id)

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")

        self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """Print the Rectangle using the `#` character.
        """
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
        """Return the print() and str() representation of
        the Rectangle.
        """
        str1 = "[Rectangle]"
        str2 = f"({self.id})"
        str3 = f"{self.__x}/{self.__y}"
        str4 = f"{self.__width}/{self.__height}"
        return str1 + " " + str2 + " " + str3 + " - " + str4

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
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
        """Return the dictionary representation
        of a Rectangle.
        """
        return ({
                    'x': self.__x,
                    'y': self.__y,
                    'id': self.id,
                    'height': self.__height,
                    'width': self.__width
                })
