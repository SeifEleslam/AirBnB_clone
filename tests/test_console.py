#!/usr/bin/python3
"""Console Test"""

from io import StringIO
import unittest

from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class TestConsole(unittest.TestCase):
    """TestConsole"""

    def test_control_cmds(self):
        """test control commands"""
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
        """test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            model = storage.all()["BaseModel."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, BaseModel)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            model = storage.all()["User."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, User)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            model = storage.all()["City."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, City)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            model = storage.all()["Place."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, Place)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            model = storage.all()["Review."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, Review)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            model = storage.all()["Amenity."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, Amenity)

    def test_all_cmd(self):
        """test all command"""
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
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            result = "["+", ".join(
                [str(val)for _, val in storage.all_cls("User").items()])+"]"
            self.assertEqual(f.getvalue().strip(), result)

    def test_show_cmd(self):
        """test show command"""
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User "+user.id))
            result = str(user)
            self.assertEqual(f.getvalue().strip(), result)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"User.show({user.id})"))
            result = str(user)
            self.assertEqual(f.getvalue().strip(), result)

    def test_count_cmd(self):
        """test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"User.count()"))
            self.assertEqual(int(f.getvalue().strip()),
                             len(storage.all_cls("User")))
