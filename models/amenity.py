#!/usr/bin/python3
"""
amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the initialization of the Amenity class
        """
        super().__init__(*args, **kwargs)
