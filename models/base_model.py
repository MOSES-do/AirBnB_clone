#!/usr/bin/env python3

"""Base Model Class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """
            constructor docstring
            If BaseModel is not called with an object argument the
            "else" part of the code is executed.
            code below uses parameter '**kwargs' which is a "dictionary"
            but creates its own created_at and updated_at by overriding
            the one present in '**kwargs' dictionary
        """

        if kwargs and len(kwargs) > 0:
            kwargs["created_at"] = datetime.now()
            kwargs["updated_at"] = datetime.now()

            for key, value in kwargs.items():
                if key != "__class__":
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

