#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        for key in storage._FileStorage__objects.keys():
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at the end of tests """
        if os.path.isfile('file.json'):
            os.remove('file.json')

    # ... (rest of your methods)

if __name__ == '__main__':
    unittest.main()
