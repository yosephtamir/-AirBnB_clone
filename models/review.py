#!/usr/bin/python
"""
THIS IS A REVIEW MODULE
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initialization of the init function
        """
        super().__init__(*args, **kwargs)
