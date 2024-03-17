#!/usr/bin/python3

"""state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class docstring"""

    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor docstring"""
        super().__init__(*args, **kwargs)
