#!/usr/bin/python3
"""Unit tests for the Review class"""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class TestReview(test_basemodel):
    """Test case for the Review class"""

    def setUp(self):
        """Set up the test case"""
        super().setUp()
        self.model = Review

    def test_place_id(self):
        """Test if the place_id attribute is of type string"""
        new_review = self.model()
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id(self):
        """Test if the user_id attribute is of type string"""
        new_review = self.model()
        self.assertEqual(type(new_review.user_id), str)

    def test_text(self):
        """Test if the text attribute is of type string"""
        new_review = self.model()
        self.assertEqual(type(new_review.text), str)

if __name__ == '__main__':
    unittest.main()
