#!/usr/bin/python3
"""test file for user class"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """test user class"""

    def setUp(self):
        """test set up of user class"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Bar")
        self.assertEqual(my_user.password, "root")

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_user = User()
        self.assertEqual(isinstance(my_user, BaseModel), True)
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_type_of_data(self):
        """test the type of data passed """
        my_user = User()
        self.assertEqual(type(my_user.email), str)
        self.assertEqual(type(my_user.password), str)
        self.assertEqual(type(my_user.first_name), str)
        self.assertEqual(type(my_user.last_name), str)

if __name__ == "__main__":
    unittest.main()
