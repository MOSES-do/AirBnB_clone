#!/usr/bin/env python3

"""city class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    def __init__(self):
        """review constrictor"""
        super().__init__()
        place_id = ""
        user_id = ""
        text = ""
