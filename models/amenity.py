#!/usr/bin/python3
"""
amenity module
"""
from models import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the initialization of the Amenity class
        """
        super().__init__(*args, **kwargs)
