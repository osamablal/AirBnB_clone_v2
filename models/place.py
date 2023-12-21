#!/usr/bin/python3
"""Defines the Place class for the HBNB project."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a place to stay with various attributes."""

    city_id = ""           # ID of the city where the place is located
    user_id = ""           # ID of the user who owns the place
    name = ""              # Name of the place
    description = ""       # Description of the place
    number_rooms = 0       # Number of rooms in the place
    number_bathrooms = 0   # Number of bathrooms in the place
    max_guest = 0          # Maximum number of guests the place can accommodate
    price_by_night = 0     # Price per night for staying at the place
    latitude = 0.0         # Latitude coordinate of the place
    longitude = 0.0        # Longitude coordinate of the place
    amenity_ids = []       # List of amenity IDs associated with the place
