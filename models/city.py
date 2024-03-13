#!/usr/bin/python3

"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    def __init__(self, *args, **kwargs):
        """city constructor"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
