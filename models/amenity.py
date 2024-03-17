#!/usr/bin/python3

"""city class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity constructor"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
