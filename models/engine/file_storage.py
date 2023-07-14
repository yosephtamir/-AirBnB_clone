#!/usr/bin/python3
"""
FileStorage module:
"""
import json
from models.base_model import BaseModel

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
            FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

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
            with open(FileStorage.__file_path) as f:
                object_content = json.load(f)
                for obj in object_content.values():
                    cls_nm = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_nm(**obj)))
        except FileNotFoundError:
            return
