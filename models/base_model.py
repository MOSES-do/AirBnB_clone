#!/usr/bin/python3

"""Base Model Class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ magic method docstring """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updated at now() docstring """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ class dictionary docstring """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
