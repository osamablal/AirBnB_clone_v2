#!/usr/bin/python3
"""Unit tests for the Amenity class"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(test_basemodel):
    """Test case for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_attribute(self):
        """Test the 'name' attribute type"""
        instance = self.value()
        self.assertEqual(type(instance.name), str)

if __name__ == '__main__':
    unittest.main()
