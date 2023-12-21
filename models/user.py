#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user with various attributes."""
    
    email = ''        # User's email address
    password = ''     # User's password
    first_name = ''   # User's first name
    last_name = ''    # User's last name
