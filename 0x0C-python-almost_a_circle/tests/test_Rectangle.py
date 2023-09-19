#!/usr/bin/python3
"""Tests cases for Rectangle class
"""
import unittest
from rectangle import Rectangle  # Assuming you have a file named rectangle.py


class TestRectangle(unittest.TestCase):
    """Test class for the Rectangle class
    """

    def test_constructor(self):
        """Test constructor
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_width_property(self):
        """Test width property
        """
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_property(self):
        """test height property
        """
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_property(self):
        """test x property
        """
        rect = Rectangle(5, 10, 2, 3)
        rect.x = 4
        self.assertEqual(rect.x, 4)

    def test_y_property(self):
        """test y property
        """
        rect = Rectangle(5, 10, 2, 3)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_area(self):
        """test area method
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test the display method
        """
        rect = Rectangle(2, 2)
        expected_output = "##\n##\n"
        self.assertEqual(rect.display(), expected_output)

    def test_str(self):
        """Test the string method
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_update_args(self):
        """Test the update argument method
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 8, 12, 4, 5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_kwargs(self):
        """Test the update kwargs argument
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(id=2, width=8, height=12, x=4, y=5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        """Test the to dictionary method
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3,
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
