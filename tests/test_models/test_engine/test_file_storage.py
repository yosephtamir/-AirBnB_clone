#!/usr/bin/python3
"""unittest for file_storage file"""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_type_of_class(self):
        """test the type of object"""
        obj = FileStorage()
        dictionaries = obj.all()
        self.assertEqual(type(dictionaries), dict)
