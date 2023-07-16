#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is a City class that inherits from base Model
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the initialization point of the City class
        """
        super().__init__(self, *args, **kwargs)
