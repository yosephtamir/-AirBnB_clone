#!/usr/bin/python3
"""test file for review class"""

from models.review import Review
from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestReview(unittest.TestCase):
    """test review class"""

    def setUp(self):
        """test set up of review class"""
        place_id = ""
        user_id = ""
        text = ""

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_review = Review()
        my_review.place_id = "B01"
        my_review.user_id = "123"
        my_review.text = "I love this"
        my_review.save()
        self.assertEqual(my_review.place_id, "B01")
        self.assertEqual(my_review.user_id, "123")
        self.assertEqual(my_review.text, "I love this")

    def test_obj_creation_date(self):
        my_review = Review()
        self.assertEqual(isinstance(my_review.created_at, datetime), True)
        self.assertEqual(isinstance(my_review.updated_at, datetime), True)

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_review = Review()
        obj_dict = my_review.to_dict()
        self.assertEqual(isinstance(my_review, BaseModel), True)
        self.assertEqual(issubclass(Review, BaseModel), True)
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(my_review.__class__.__name__, "Review")

    def test_type_of_data(self):
        """test the type of data passed """
        my_review = Review()
        self.assertEqual(type(my_review.place_id), str)
        self.assertEqual(type(my_review.user_id), str)
        self.assertEqual(type(my_review.text), str)


if __name__ == "__main__":
    unittest.main()
