#!/usr/bin/python3
"""File Storage Class Test"""

import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        storage = FileStorage()
        test = storage.all()
        self.assertEqual(storage.all(), test)

    @patch('os.path.exists')
    def test_all_no_file(self, mock_path_exists):
        storage = FileStorage()
        test = storage.all()
        mock_path_exists.return_value = False
        model = BaseModel()
        model.save()
        storage.reload()
        self.assertEqual(storage.all(), test)

    def test_all_with_file(self):
        storage = FileStorage()
        model = BaseModel()
        model.save()
        storage.reload()
        self.assertEqual(
            storage.all()[f"BaseModel.{model.id}"].
            to_dict(), model.to_dict())

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        test = storage.all().copy()
        test[f'{obj.__class__.__name__}.{obj.id}'] = obj
        storage.new(obj)
        self.assertEqual(storage.all(), test)

    def test_save(self):
        storage = FileStorage()
        storage.new(
            BaseModel())
        with patch("builtins.open"):
            storage.save()
            open.assert_called_once_with("file.json", "w")
