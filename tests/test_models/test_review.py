#!/usr/bin/python3
"""Review Test"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = Review()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(model.created_at, model.updated_at)
