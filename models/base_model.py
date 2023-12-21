#!/usr/bin/python3
"""Defines a base class for all models in our HBNB clone."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all HBNB models."""
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance."""
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current time when the instance is changed."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the instance into a dictionary format."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
