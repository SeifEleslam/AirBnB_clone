#!/usr/bin/python3
"""Console Test"""

from io import StringIO
import unittest

from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """TestConsole"""

    def test_control_cmds(self):
        output = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "Handles EOF (Ctrl+D) to exit the shell"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "Create command"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "Show command"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "List all instances of a class"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "Update an attribute value for an object"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(f.getvalue().strip(), output)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual(f.getvalue().strip(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(f.getvalue().strip(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
            self.assertEqual(f.getvalue().strip(), "")

    def test_create_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            model = storage.all()["BaseModel."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, BaseModel)

    def test_all_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            result = "["+", ".join([str(val)
                                    for _, val in storage.all().items()])+"]"
            self.assertEqual(f.getvalue().strip(), result)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            result = "["+", ".join(
                [str(val)for _, val in storage.all_cls("User").items()])+"]"
            self.assertEqual(f.getvalue().strip(), result)
