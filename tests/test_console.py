#!/usr/bin/python3
"""Console Test"""

from io import StringIO
import unittest

from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """TestConsole"""

    def test_control_cmds(self):
        cmd = HBNBCommand()
        self.assertEqual(cmd.prompt, "(hbnb) ")
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
        output = '*** Unknown syntax: sad'
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('sad'))
            self.assertEqual(f.getvalue().strip(), output)

    def test_create_cmd(self):
        """test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            model = storage.all()["BaseModel."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, BaseModel)
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseMode"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(f.getvalue().strip(), output)

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
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseMode"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("base.all()"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class name missing **"

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
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseMode"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel sad"))
            self.assertEqual(f.getvalue().strip(), output)

    def test_count_cmd(self):
        """test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"User.count()"))
            self.assertEqual(int(f.getvalue().strip()),
                             len(storage.all_cls("User")))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f".count()"))
            self.assertEqual(int(f.getvalue().strip()),
                             len(storage.all()))
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("sad.count()"))
            self.assertEqual(f.getvalue().strip(), output)

    def test_destroy_cmd(self):
        """test destroy command"""
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User "+user.id))
            with self.assertRaises(KeyError):
                storage.all()[f"User.{user.id}"]
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"User.destroy({user.id})"))
            with self.assertRaises(KeyError):
                storage.all()[f"User.{user.id}"]
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("sad.destroy()"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy sad"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User sad"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(sad)"))
            self.assertEqual(f.getvalue().strip(), output)

    def test_update_cmd(self):
        """test update command"""
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "update User "+user.id+" first_name sa3d"))
            self.assertEqual(
                storage.all()[f"User.{user.id}"].first_name, 'sa3d')
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "User.update("+user.id+", first_name, 'sa3d')"))
            self.assertEqual(
                storage.all()[f"User.{user.id}"].first_name, 'sa3d')
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "User.update('"+user.id+"', age, 89)"))
            new_user = storage.all()[f"User.{user.id}"]
            self.assertIsInstance(new_user.age, int)
            self.assertEqual(new_user.age, 89)
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "User.update("+user.id+", {'first_name' : 'sa3d'})"))
            self.assertEqual(
                storage.all()[f"User.{user.id}"].first_name, 'sa3d')
        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "User.update('"+user.id+"',{ 'age': 89})"))
            new_user = storage.all()[f"User.{user.id}"]
            self.assertIsInstance(new_user.age, int)
            self.assertEqual(new_user.age, 89)
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                "User.update('123', first_name , 89)"))
            self.assertEqual(f.getvalue().strip(), output)
        user = User()
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                f"Use.update('{user.id}', first_name , 89)"))
            self.assertEqual(f.getvalue().strip(), output)
        user = User()
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                f"User.update(, first_name , 89)"))
            self.assertEqual(f.getvalue().strip(), output)
        user = User()
        output = "** attribute name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                f"User.update({user.id},  , 89)"))
            self.assertEqual(f.getvalue().strip(), output)
        user = User()
        output = "** value missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(
                f"User.update({user.id},  sad, )"))
            self.assertEqual(f.getvalue().strip(), output)
