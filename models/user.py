#!/usr/bin/env python3

"""User Class"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Structure of user class"""

    def __init__(self):
        """ constructor method """
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
