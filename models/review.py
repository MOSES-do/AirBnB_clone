#!/usr/bin/python3

"""city class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """review constructor"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('Place.id', '')
        self.user_id = kwargs.get('User.id', '')
