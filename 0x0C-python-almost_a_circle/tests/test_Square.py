#!/usr/bin/python3
"""Tests for the Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class
    """
    def test_constructor(self):
        """Test the constructor/instance method
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_property(self):
        """Test the size property
        """
        square = Square(5)
        square.size = 15
        self.assertEqual(square.size, 15)

    def test_str(self):
        """Test the string method
        """
        square = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_update_args(self):
        """Test the update arguments method
        """
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        """Test the update keywords argument method
        """
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=8, x=4, y=5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        """Test the to dictionary method
        """
        square = Square(5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3,
        }
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
