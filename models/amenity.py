#!/usr/bin/python3
"""Amenity Module for HBNB project."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class representing various amenities."""
    
    name = ""  # Name of the amenity
