#!/usr/bin/python3
"""test file for place class"""

from models.place import Place
from models.base_model import BaseModel
import unittest
from datetime import datetime

class Testplace(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """test set up of place class"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def test_attr_of_class(self):
        """test class attributes assignment"""
        my_place = Place()
        my_place.city_id = "123"
        my_place.user_id = "123"
        my_place.name = "ADD"
        my_place.description = "testing"
        my_place.number_rooms = 30
        my_place.number_bathrooms = 60
        my_place.max_guest = 1000
        my_place.price_by_night = 5000
        my_place.latitude = 30
        my_place.longitude = 15
        my_place.save()
        self.assertEqual(my_place.city_id, "123")
        self.assertEqual(my_place.user_id, "123")
        self.assertEqual(my_place.name, "ADD")
        self.assertEqual(my_place.description, "testing")
        self.assertEqual(my_place.number_rooms, 30)
        self.assertEqual(my_place.number_bathrooms, 60)
        self.assertEqual(my_place.latitude, 30)
        self.assertEqual(my_place.longitude, 15)

    def test_obj_creation_date(self):
        my_place = Place()
        self.assertEqual(isinstance(my_place.created_at, datetime), True)
        self.assertEqual(isinstance(my_place.updated_at, datetime), True)

    def test_inher_of_class(self):
        """test inheritance of the class from BaseModel"""
        my_place = Place()
        obj_dict = my_place.to_dict()
        self.assertEqual(isinstance(my_place, BaseModel), True)
        self.assertEqual(issubclass(Place, BaseModel), True)
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(my_place.__class__.__name__, "Place")

    def test_type_of_data(self):
        """test the type of data passed """
        my_place = Place()
        self.assertEqual(type(my_place.city_id), str)
        self.assertEqual(type(my_place.user_id), str)
        self.assertEqual(type(my_place.name), str)
        self.assertEqual(type(my_place.description), str)
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertEqual(type(my_place.number_bathrooms), int)
        self.assertEqual(type(my_place.latitude), float)
        self.assertEqual(type(my_place.longitude), float)
        self.assertEqual(type(my_place.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
