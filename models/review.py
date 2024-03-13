#!/usr/bin/python3

"""city class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    def __init__(self, *args, **kwargs):
        """review constrictor"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')
