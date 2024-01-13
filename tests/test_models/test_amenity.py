#!/usr/bin/python3
"""Amenity Test"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestAmenity"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = Amenity()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(model.created_at, model.updated_at)
