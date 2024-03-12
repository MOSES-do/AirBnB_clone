#!/usr/bin/env python3

"""city class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity constructor"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
