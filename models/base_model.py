#!/usr/bin/python3
"""
Base class of the project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all iclasses
    define arguments using:
    args: not supported by now
    kwargs: dictionary that contains info
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, dateformat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """return string presentation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save class instances
        not yet done
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return dictionary presentation of class
        created_at and updated_at: all are updated
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
