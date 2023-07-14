#!/usr/bin/python3
"""
Base class where other class inherit from
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    Base class for all classes
    define arguments using:
        args: not supported by now
        kwargs: dictionary that contains info
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if not kwargs:
            storage.new(self)
        else:
            for key, values in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dateformat = "%Y-%m-%dT %H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(values, dateformat)
                else:
                    self.__dict__[key] = values

    def __str__(self):
        """return string presentation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save class instances
        not yet done
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """return dictionary presentation of class
        created_at and updated_at: all are updated
        """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
