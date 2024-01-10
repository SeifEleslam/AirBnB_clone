#!/usr/bin/python3
"""State Test"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """TestState"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = State()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.created_at, model.updated_at)
