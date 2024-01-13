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
        # self.assertEqual(storage.__file_path, test_file)

    @patch('os.path.exists')
    def test_all_no_file(self, mock_path_exists):
        storage = FileStorage()
        mock_path_exists.return_value = False
        self.assertEqual(storage.all(), dict())

    @patch('builtins.open')
    def test_all_with_file(self, mock_open):
        storage = FileStorage()
        test = storage.all().copy()
        test['key'] = "value"
        mock_open.return_value.__enter__.\
            return_value.read.return_value = '{"key": "value"}'
        storage.reload()
        self.assertEqual(storage.all(), {"key": "value"})

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        test = storage.all().copy()
        test[f'{obj.__class__.__name__}.{obj.id}'] = obj.to_dict()
        storage.new(obj)
        self.assertEqual(storage.all(), test)

    def test_save(self):
        storage = FileStorage()
        storage.new(
            BaseModel())
        with patch("builtins.open"):
            storage.save()
            open.assert_called_once_with("file.json", "w")
