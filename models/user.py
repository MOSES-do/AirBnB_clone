#!/usr/bin/python3

"""User Class"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Structure of user class"""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
