#!/usr/bin/python3
"""Unit tests for the Place class"""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class TestPlace(test_basemodel):
    """Test case for the Place class"""

    def setUp(self):
        """Set up the test case"""
        super().setUp()
        self.model = Place

    def test_city_id(self):
        """Test if the city_id attribute is of type string"""
        new_place = self.model()
        self.assertEqual(type(new_place.city_id), str)

    def test_user_id(self):
        """Test if the user_id attribute is of type string"""
        new_place = self.model()
        self.assertEqual(type(new_place.user_id), str)

    def test_name(self):
        """Test if the name attribute is of type string"""
        new_place = self.model()
        self.assertEqual(type(new_place.name), str)

    def test_description(self):
        """Test if the description attribute is of type string"""
        new_place = self.model()
        self.assertEqual(type(new_place.description), str)

    def test_number_rooms(self):
        """Test if the number_rooms attribute is of type int"""
        new_place = self.model()
        self.assertEqual(type(new_place.number_rooms), int)

    def test_number_bathrooms(self):
        """Test if the number_bathrooms attribute is of type int"""
        new_place = self.model()
        self.assertEqual(type(new_place.number_bathrooms), int)

    def test_max_guest(self):
        """Test if the max_guest attribute is of type int"""
        new_place = self.model()
        self.assertEqual(type(new_place.max_guest), int)

    def test_price_by_night(self):
        """Test if the price_by_night attribute is of type int"""
        new_place = self.model()
        self.assertEqual(type(new_place.price_by_night), int)

    def test_latitude(self):
        """Test if the latitude attribute is of type float"""
        new_place = self.model()
        self.assertEqual(type(new_place.latitude), float)

    def test_longitude(self):
        """Test if the longitude attribute is of type float"""
        new_place = self.model()
        self.assertEqual(type(new_place.longitude), float)

    def test_amenity_ids(self):
        """Test if the amenity_ids attribute is of type list"""
        new_place = self.model()
        self.assertEqual(type(new_place.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
