#!/usr/bin/python3
"""Test for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class
    """

    def test_constructor_with_id(self):
        """Test constructor with ID
        """
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        """Test constructor without ID
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        """Test to json string method
        """
        obj = Base()
        self.assertEqual(obj.to_json_string(None), '[]')

    def test_save_to_file(self):
        """Test save to file method
        """
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """Test from json string method
        """
        json_string = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1}, {"id": 2}])

    def test_create(self):
        """test the create method
        """
        dictionary = {"id": 3}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 3)

    def test_load_from_file(self):
        """Test load from file method
        """
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

    def test_save_to_file_csv(self):
        """Test save to file csv method
        """
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file_csv([obj1, obj2])
        with open("Base.csv", "r") as file:
            content = file.read()
            self.assertTrue(content.startswith("id\n1\n2"))

    def test_load_from_file_csv(self):
        """Test load from file method
        """
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file_csv([obj1, obj2])
        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)


if __name__ == '__main__':
    unittest.main()
