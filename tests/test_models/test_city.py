#!/usr/bin/python3
"""test file for city class"""

from models.city import City
from models.base_model import BaseModel
import unittest

class Testcity(unittest.TestCase):
    """test city class"""

    def setUp(self):
        """test set up of city class"""
        name = ""
        state_id = ""

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_city = City()
        my_city.state_id = "1234"
        my_city.name = "Betty"
        my_city.save()
        self.assertEqual(my_city.name, "Betty")
        self.assertEqual(my_city.state_id, "1234")

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_city = City()
        self.assertEqual(isinstance(my_city, BaseModel), True)
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_type_of_data(self):
        """test the type of data passed """
        my_city = City()
        self.assertEqual(type(my_city.name), str)
        self.assertEqual(type(my_city.state_id), str)


if __name__ == "__main__":
    unittest.main()
