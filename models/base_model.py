#!/usr/bin/python3
"""
Base class where other class inherit from
"""

from uuid import uuid4
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
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    # def __init__(self, *args, **kwargs):
    #     if not kwargs:
    #         self.id = str(uuid.uuid4())
    #         self.created_at = datetime.now()
    #         self.updated_at = datetime.now()
    #     else:
    #         for key, values in kwargs.items():
    #             if key == 'created_at' or key == 'updated_at':
    #                 dateformat = "%Y-%m-%dT %H:%M:%S.%f"
    #                 values = datetime.strptime(kwargs[key], dateformat)
    #             if key != '__class__':
    #                 setattr(self, key, values)

    def __str__(self):
        """return string presentation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save class instances
        not yet done
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """return dictionary presentation of class
        created_at and updated_at: all are updated
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
        # new_dict = self.__dict__
        # new_dict["__class__"] = self.__class__.__name__
        # dateformat = "%Y-%m-%dT %H:%M:%S.%f"
        # new_dict["created_at"] = self.created_at.strftime(dateformat)
        # new_dict["updated_at"] = self.updated_at.strftime(dateformat)
        # return new_dict
