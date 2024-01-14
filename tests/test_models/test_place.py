#!/usr/bin/python3
"""Place Model Test"""

import unittest
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace"""

    def test_instantiation_with_no_args(self):
        """Test instantiating with no arguments."""
        model = Place()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertIsInstance(model.user_id, str)
        self.assertIsInstance(model.name, str)
        self.assertIsInstance(model.description, str)
        self.assertIsInstance(model.number_rooms, int)
        self.assertIsInstance(model.number_bathrooms, int)
        self.assertIsInstance(model.latitude, float)
        self.assertIsInstance(model.longitude, float)
        self.assertIsInstance(model.amenity_ids, list)

    def test_instantiation_with_kwargs(self):
        """Test instantiating with keyword arguments."""
        model = Place()
        model.first_name = "first_name"
        model.last_name = "last_name"
        model.email = "email"
        model.password = "password"
        key_model = Place(**model.to_dict())
        self.assertEqual(model.first_name, key_model.first_name)
        self.assertEqual(model.last_name, key_model.last_name)
        self.assertEqual(model.password, key_model.password)
        self.assertEqual(model.email, key_model.email)

    def test_save_method(self):
        """Test the save method updates updated_at."""
        model = Place()
        model.name = "My Model"
        model.number = 89
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertGreater(model.updated_at, original_updated_at)
        updated_model = Place(
            **storage.all()[model.__class__.__name__+'.'+model.id].to_dict())
        self.assertEqual(updated_model.updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method produces the expected dictionary."""
        model = Place()
        model.name = "My Model"
        model.number = 89
        model.first_name = "sad"
        model_dict = model.to_dict()
        expected_keys = ['id', 'created_at',
                         'updated_at', '__class__', 'name', 'number',
                         'first_name']
        self.assertEqual(set(model_dict.keys()), set(expected_keys))
        self.assertEqual(model_dict['__class__'], 'Place')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model.name, model_dict['name'])
        self.assertEqual(model.number, model_dict['number'])
