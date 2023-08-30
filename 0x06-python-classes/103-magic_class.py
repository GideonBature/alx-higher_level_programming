#!/usr/bin/python3

"""Module defines a MagicClass that reps a circle with radius"""

import math

"""import math"""


class MagicClass:
    """
    A class represents a circle, provides methods to cal area & circumference.

    Attributes:
        _MagicClass__radius (int or float): The radius of the circle.

    Methods:
        Constructor initialize circle w/radius.
        area(self): Calculate the area of the circle.
        circumference(self): Calculate the circumference of the circle.
    """

    def __init__(self, _MagicClass__radius=0):
        """Initialize the MagicClass with a given radius.

        Args:
            _MagicClass__radius (int or float): radius of circle.

        Raises:
            TypeError: If the provided radius is not a number.
        """

        if ((type(_MagicClass__radius) is not int) and
                (type(_MagicClass__radius) is not float)):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = _MagicClass__radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (math.pi * self._MagicClass__radius ** 2)

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self._MagicClass__radius)
