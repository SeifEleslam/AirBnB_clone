#!/usr/bin/python3
"""Base Model Test"""

import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """TestBaseModal"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_instantiation_with_kwargs(self):
        """Test instantiating with keyword arguments."""
        now = datetime.now()
        created_at = now - timedelta(hours=1)
        kwargs = {'created_at': created_at.isoformat(),
                  'updated_at': now.isoformat()}
        model = BaseModel(**kwargs)
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, now)

    def test_save_method(self):
        """Test the save method updates updated_at."""
        model = BaseModel()
        model.name = "My Model"
        model.number = 89
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertGreater(model.updated_at, original_updated_at)
        updated_model = BaseModel(
            **storage.all()[model.__class__.__name__+'.'+model.id])
        self.assertEqual(updated_model.updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method produces the expected dictionary."""
        model = BaseModel()
        model.name = "My Model"
        model.number = 89
        model_dict = model.to_dict()
        expected_keys = ['id', 'created_at',
                         'updated_at', '__class__', 'name', 'number']
        self.assertEqual(set(model_dict.keys()), set(expected_keys))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model.name, model_dict['name'])
        self.assertEqual(model.number, model_dict['number'])
