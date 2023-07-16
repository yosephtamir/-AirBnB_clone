#!/usr/bin/python3
"""
This is used to hold the state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from Base Model
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is used to initialize the State class
        """
        super().__init__(*args, **kwargs)
