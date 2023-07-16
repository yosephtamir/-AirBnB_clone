#!/usr/bin/python3
"""Unittest of base_model file
it is based on BaseModel class"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test for basemodel class"""

    def test_output_of_class_attributes(self):
        """test for attr values"""
        obj = BaseModel()
        obj.name = "Eugene"
        obj.number = 89
        obj.save()
        obj_dict = obj.to_dict()
        self.assertEqual(obj.name, "Eugene")
        self.assertEqual(obj.number, 89)

    def test_type_of_class(self):
        """tester for typ of instances"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)
        self.assertEqual(type(obj_dict), dict)


if __name__ == "__main__":
    unittest.main()
