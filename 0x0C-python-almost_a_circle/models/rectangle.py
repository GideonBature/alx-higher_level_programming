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
    def get_width(self):
        return self.__width

    @get_width.setter
    def set_width(self, value):
        self.__width = value

    @property
    def get_height(self):
        return self.__height

    @get_height.setter
    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @get_width.setter
    def set_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    @get_height.setter
    def set_y(self, value):
        self.__y = value
