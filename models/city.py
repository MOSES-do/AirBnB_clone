#!/usr/bin/python3

"""city class"""
from models.state import State


class City(State):
    """city class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """city constructor"""
        super().__init__(*args, **kwargs)
        """
            Retrieve the value associated with the key 'name'
            from kwargs, defaulting to '' if not found
        """
        self.state_id = kwargs.get('State.id', '')
