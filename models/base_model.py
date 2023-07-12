#!/usr/bin/python3
"""
Base class where other class inherit from
"""

import uuid
import datetime

class BaseModel:
    """
    Base class for all classes
    define arguments using:
        args: not supported by now
        kwargs: dictionary that contains info
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, values in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dateformat = "%Y-%m-%dT %H:%M:%S.%f"
                    values = datetime.datetime.strptime(kwargs[key], dateformat)
                if (key != '__class__'):
                    setattr(self, key, values)

    def __str__(self):
        """return string presentation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save class instances
        not yet done
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """return dictionary presentation of class
        created_at and updated_at: all are updated
        """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT %H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
