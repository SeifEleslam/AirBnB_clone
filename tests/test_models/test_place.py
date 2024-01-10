#!/usr/bin/python3
"""Place Test"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = Place()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.created_at, model.updated_at)
