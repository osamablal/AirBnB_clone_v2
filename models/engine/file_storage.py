#!/usr/bin/python3
"""This module defines a class to manage file storage for HBNB clone."""
import json


class FileStorage:
    """This class manages storage of HBNB models in JSON format."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all()[key] = obj

    def save(self):
        """Saves the storage dictionary to a file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: val.to_dict() for key, val in self.all().items()}
            json.dump(temp, f)

    def reload(self):
        """Loads the storage dictionary from a file."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    self.all()[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass
