#!/usr/bin/env python3

""" File Storage class """
import json
import os
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects """
        return FileStorage.__objects

    def new(self, obj):
        """ new object """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ method saves class obj dict into new_dict
            and creates a JSON readable format file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f, indent=4)

    def reload(self):
        """loads user data from json file, parse it and
            pass it to base model as a dictionary which is converted
            to a python object
        """
        try:
            with open(self.__file_path, "r") as f:
                json_str = json.load(f)
                for key, value in json_str.items():
                    class_name = (value['__class__'])
                    cls = globals()[class_name]
                    py = cls(**value)
                    FileStorage.__objects[key] = py
        except FileNotFoundError:
            pass
