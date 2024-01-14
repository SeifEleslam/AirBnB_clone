#!/usr/bin/python3
"""File Storage Class Test"""

import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to test the file storage class."""

    def setUp(self):
        """Set up the test environment"""
        storage = FileStorage()
        test = storage.all()
        self.assertEqual(storage.all(), test)

    @patch('os.path.exists')
    def test_all_no_file(self, mock_path_exists):
        """Test all method if no file exists."""
        storage = FileStorage()
        test = storage.all()
        mock_path_exists.return_value = False
        model = BaseModel()
        model.save()
        storage.reload()
        self.assertEqual(storage.all(), test)

    def test_all_with_file(self):
        """Tests that the all method returns a list of objects in the file."""
        storage = FileStorage()
        model = BaseModel()
        self.assertEqual(
            storage.all()[f"BaseModel.{model.id}"], model)
        model.save()
        storage.reload()
        self.assertEqual(
            storage.all()[f"BaseModel.{model.id}"].
            to_dict(), model.to_dict())
        self.assertIsInstance(
            storage.all()[f"BaseModel.{model.id}"], BaseModel)

    def test_new(self):
        """test new value in BaseModel"""
        storage = FileStorage()
        obj = BaseModel()
        test = storage.all().copy()
        test[f'{obj.__class__.__name__}.{obj.id}'] = obj
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), len(test))
        self.assertEqual((storage.all().keys()), (test.keys()))

    def test_save(self):
        """Test Saving process"""
        storage = FileStorage()
        model = BaseModel()
        with patch("builtins.open"):
            storage.save()
            open.assert_called_once_with("file.json", "w")

    def test_del(self):
        """Test deleting process"""
        storage = FileStorage()
        model = BaseModel()
        storage.delete(f"BaseMode.{model.id}")
        self.assertFalse(f"BaseMode.{model.id}" in storage.all())
