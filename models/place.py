#!/usr/bin/python3

"""city class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place constructor"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_barthrooms = 0
    new_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """place constructor:"""
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get("City.id", '')
        self.user_id = kwargs.get("User.id", '')
