#!/usr/bin/python3
"""test file for amenity class"""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest

class Testamenity(unittest.TestCase):
    """test amenity class"""

    def setUp(self):
        """test set up of amenity class"""
        name = ""

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_amenity = Amenity()
        my_amenity.name = "Betty"
        my_amenity.save()
        self.assertEqual(my_amenity.name, "Betty")

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_amenity = Amenity()
        self.assertEqual(isinstance(my_amenity, BaseModel), True)
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_type_of_data(self):
        """test the type of data passed """
        my_amenity = Amenity()
        self.assertEqual(type(my_amenity.name), str)


if __name__ == "__main__":
    unittest.main()
