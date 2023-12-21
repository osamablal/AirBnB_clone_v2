#!/usr/bin/python3
"""Defines the Review class for the HBNB project."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a review with various attributes."""

    place_id = ""  # ID of the place being reviewed
    user_id = ""   # ID of the user who wrote the review
    text = ""      # Text content of the review
