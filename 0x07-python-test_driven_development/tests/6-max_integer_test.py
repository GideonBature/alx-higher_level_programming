#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function.
    """

    def test_empty_list(self):
        """Test when the input list is empty.
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test when the input list contains a single element.
        """
        self.assertEqual(max_integer([10]), 10)

    def test_positive_elements(self):
        """Test when the input list contains positive integers.
        """
        self.assertEqual(max_integer([1, 0, 23, 81, 25, 6]), 81)

    def test_negative_elements(self):
        """Test when the input list contains negative integers.
        """
        self.assertEqual(max_integer([-5, -8, -12, -6, -2]), -2)

    def tes_mixed_elements(self):
        """Test when the input list contains a mix of +ve & -ve integers.
        """
        self.assertEqual(max_integer([5, 3, -7, -6, 8, -2, 4]), 8)

    def test_duplicate_maximum(self):
        """Test when the input list contains duplicate maximum values.
        """
        self.assertEqual(max_integer([8, 5, 2, 3, 8, 4, 8]), 8)
        self.assertEqual(max_integer([-2, -2, -5, -8, -2, -7]), -2)

    def test_contains_zero(self):
        """Test when the input list contains zero values.
        """
        self.assertEqual(max_integer([0, 8, 5, 4, 7, 3]), 8)
        self.assertEqual(max_integer([-2, -5, -8, -3, 0, -1]), 0)

    def test_mixed_data_types(self):
        """Test when the input list contains a mix of integers and floats.
        """
        self.assertEqual(max_integer([2, 1, 4.5, 8, 2]), 8)
        self.assertEqual(max_integer([-5, -1, -9.5, -8]), -1)

    def test_float_data_type(self):
        """Test when the input list contains only floating-point numbers.
        """
        self.assertEqual(max_integer([3.5, 4.2, 8.5, 8.7, 7.6]), 8.7)
        self.assertEqual(max_integer([-3.7, -8.9, -2.1, -5.2, -1.5]), -1.5)

    def test_non_integer_elements(self):
        """Test when the input list contains non-integer elements (TypeError).
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 8, 2])
        with self.assertRaises(TypeError):
            max_integer([2.5, '3.6', 5.4])
        with self.assertRaises(TypeError):
            max_integer([2, None, 5])
        with self.assertRaises(TypeError):
            max_integer([2.5, 3.6, None, 5.4])


if __name__=='__main__':
    unittest.main()
