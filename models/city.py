#!/usr/bin/python3
"""Defines the City class for the HBNB project."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city with state ID and name."""

    state_id = ""  # ID of the state to which the city belongs
    name = ""      # Name of the city
