#!/usr/bin/python3
"""Square Class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class with private instances
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        Raises:
            TypeError: If size is not an int.
            ValueError: if size <= 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square.
        Args:
            value (int): The new size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation
        of a Square.
        """
        str1 = "[Square]"
        str2 = f"({self.id})"
        str3 = f"{self.__x}/{self.__y}"
        str4 = f"{self.__size}"
        return str1 + " " + str2 + " " + str3 + " - " + str4

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
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

    def to_dictionary(self):
        """Return the dictionary representation of the Square.
        """
        return ({
                    'id': self.id,
                    'x': self.__x,
                    'size': self.__size,
                    'y': self.__y
                })
