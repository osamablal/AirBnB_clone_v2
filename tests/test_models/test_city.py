#!/usr/bin/python3
"""Unit tests for the City class"""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class TestCity(test_basemodel):
    """Test case for the City class"""

    def setUp(self):
        """Set up the test case"""
        super().setUp()
        self.model = City

    def test_state_id(self):
        """Test if the state_id attribute is of type string"""
        new_city = self.model()
        self.assertEqual(type(new_city.state_id), str)

    def test_name(self):
        """Test if the name attribute is of type string"""
        new_city = self.model()
        self.assertEqual(type(new_city.name), str)

if __name__ == '__main__':
    unittest.main()
