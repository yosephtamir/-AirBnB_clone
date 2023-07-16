#!/usr/bin/python3
"""
FileStorage module:
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
     a class FileStorage that serializes instances to a JSON file and
     deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            FileStorage.__objects[obj.__class__.__name__ + "." +
                                  str(obj.id)] = obj

    def save(self):
        """
        method serializes __objects to the JSON file
        """
        Ocopy = FileStorage.__objects
        obj_dict = {obj: Ocopy[obj].to_dict() for obj in Ocopy.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        This method deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as file:
                dict_obj = json.load(file)
                for obj in dict_obj.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
