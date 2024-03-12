#!/usr/bin/env python3

"""state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class docstring"""
    def __init__(self, *args, **kwargs):
        """State constructor docstring"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
