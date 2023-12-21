#!/usr/bin/python3
"""Defines the State class for the HBNB project."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state with various attributes."""

    name = ""  # The name of the state
