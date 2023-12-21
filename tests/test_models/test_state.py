#!/usr/bin/python3
"""Unit tests for the State class"""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class TestState(test_basemodel):
    """Test case for the State class"""

    def setUp(self):
        """Set up the test case"""
        super().setUp()
        self.model = State

    def test_name(self):
        """Test if the name attribute is of type string"""
        new_state = self.model()
        self.assertEqual(type(new_state.name), str)

if __name__ == '__main__':
    unittest.main()
