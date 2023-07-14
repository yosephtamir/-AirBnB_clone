#!/usr/bin/python3
"""
FileStorage module:
"""
import json

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
        This method serializes __objects to the JSON file (path: __file_path)
        """

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
        # with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
        #     new_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        #     json.dump(new_dict, file)
            
        # objectCopy  = FileStorage.__objects
        # for obj in objectCopy.keys():
        #     new_dict = {obj: objectCopy[obj].to_dict()}
        # with open(FileStorage.__file_path, "w") as file:
        #     json.dump(new_dict, file)
        
    def reload(self):
        """
        This method deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

        # try:
        #     with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
        #         content = json.load(file)
        #         print(content)
        # except FileNotFoundError:
        #     return
