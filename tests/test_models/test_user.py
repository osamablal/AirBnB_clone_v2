#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(test_basemodel):
    """Test case for the User class"""

    def setUp(self):
        """Set up the test case"""
        super().setUp()
        self.model = User

    def test_first_name(self):
        """Test if the first_name attribute is of type string"""
        new_user = self.model()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name(self):
        """Test if the last_name attribute is of type string"""
        new_user = self.model()
        self.assertEqual(type(new_user.last_name), str)

    def test_email(self):
        """Test if the email attribute is of type string"""
        new_user = self.model()
        self.assertEqual(type(new_user.email), str)

    def test_password(self):
        """Test if the password attribute is of type string"""
        new_user = self.model()
        self.assertEqual(type(new_user.password), str)

if __name__ == '__main__':
    unittest.main()
