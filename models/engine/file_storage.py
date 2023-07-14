#!/usr/bin/python3
"""
FileStorage module:
"""
import json
import models
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
        return self.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            i = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[i] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file (path: __file_path)
        """
        new = {}
        for i in self.__objects:
            new[i] = self.__objects[i].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new, file)

    def reload(self):
        """
        This method deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)
        except Exception:
            return
