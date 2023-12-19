#!/usr/bin/python3
"""
The modele gives an object to store as a type
having the modele of the objects.
"""
from os import getenv
import models.engine

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = models.engine.db_storage.DBStorage()
else:
    storage = models.engine.file_storage.FileStorage()

storage.reload()

