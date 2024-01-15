#!/usr/bin/python3
"""
Class Place inherits from BaseModel
"""


import uuid
from models.base_model import BaseModel
import datetime


class Place(BaseModel):
    """
    Class Place definition
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        super().__init__(*args, **kwargs)
