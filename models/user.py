#!/usr/bin/python3
"""
This Module is used to show users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A user identfier class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialization point
        """
        super().__init__(self, *args, **kwargs)
