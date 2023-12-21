#!/usr/bin/python3
"""Unit tests for the BaseModel class"""

from models.base_model import BaseModel
import unittest
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up the test case"""
        pass

    def tearDown(self):
        """Clean up after the test case"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test creating an instance with the default constructor"""
        instance = self.value()
        self.assertIsInstance(instance, self.value)

    def test_kwargs(self):
        """Test creating an instance with a dictionary of attributes"""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertIsNot(new_instance, instance)

    # ... Other test methods ...

    def test_updated_at(self):
        """Test the 'updated_at' attribute"""
        instance = self.value()
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        initial_updated_at = instance.updated_at
        serialized_instance = instance.to_dict()
        new_instance = BaseModel(**serialized_instance)
        self.assertNotEqual(new_instance.updated_at, initial_updated_at)

if __name__ == '__main__':
    unittest.main()
