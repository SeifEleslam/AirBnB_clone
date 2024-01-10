#!/usr/bin/python3
"""City Test"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = City()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.created_at, model.updated_at)
