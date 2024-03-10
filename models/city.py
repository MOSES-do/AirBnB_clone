#!/usr/bin/env python3

"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    def __init__(self):
        """city constructor"""
        super().__init__()
        state_id = ""
        name = ""
