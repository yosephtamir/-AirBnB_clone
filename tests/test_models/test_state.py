#!/usr/bin/python3
"""test file for state class"""

from models.state import State
from models.base_model import BaseModel
import unittest
from datetime import datetime

class Teststate(unittest.TestCase):
    """test state class"""

    def setUp(self):
        """test set up of state class"""
        name = ""

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_state = State()
        my_state.name = "state"
        my_state.save()
        self.assertEqual(my_state.name, "state")

    def test_obj_creation_date(self):
        my_state = State()
        self.assertEqual(isinstance(my_state.created_at, datetime), True)
        self.assertEqual(isinstance(my_state.updated_at, datetime), True)

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_state = State()
        obj_dict = my_state.to_dict()
        self.assertEqual(isinstance(my_state, BaseModel), True)
        self.assertEqual(issubclass(State, BaseModel), True)
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(my_state.__class__.__name__, "State")

    def test_type_of_data(self):
        """test the type of data passed """
        my_state = State()
        self.assertEqual(type(my_state.name), str)


if __name__ == "__main__":
    unittest.main()
