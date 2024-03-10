#!/usr/bin/env python3

"""city class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place constructor"""
    def __init__(self):
        """place constructor:"""
        super().__init__()
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        new_guest = 0
        price_by_night = 0
        latitude = 0.0
        lonfitude = 0.0
        amenity_ids = []
