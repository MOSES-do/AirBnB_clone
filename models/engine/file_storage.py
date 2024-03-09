#!/usr/bin/env python3

""" File Storage class """
import json
import os
import models.base_model as b


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects """
        return self.__objects

    def new(self, obj):
        """ new object """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ method saves class obj dict into new_dict
            and creates a JSON readable format file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

            with open(self.__file_path, "w", encoding="UTF-8") as f:
                json.dump(new_dict, f, indent=4)

    def reload(self):
        """loads user data from json file, parse it and
            pass it to base model as a dictionary which is converted
            to a python object
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_str = json.load(f)
                for key, value in json_str.items():
                    """print(f"str......{value}")"""
                    jsonToPythonObj = b.BaseModel(**value)
                    self.__objects[key] = jsonToPythonObj
                    """print(f"{jsonToPythonObj}")"""
        else:
            pass

