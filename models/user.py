#!/usr/bin/python3

"""User Class"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Structure of user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(*args, **kwargs)
