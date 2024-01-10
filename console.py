#!/usr/bin/python3
"""Base Model Class Test"""

from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


from models import storage


class HBNBCommand(Cmd):
    """HBNB Command Shell"""

    prompt = "(hbnb) "

    @staticmethod
    def cmd_options(line: str, num: int) -> set[str]:
        """Return the options for a command line."""
        options = [item for item in line.split(" ") if item]
        options = [options[i] if i < len(
            options) else None for i in range(num)]
        return options

    @staticmethod
    def check_cls(cls: str) -> bool:
        """Check Class"""
        try:
            globals()[cls]
            return True
        except KeyError:
            return False

    @staticmethod
    def check_id(cls: str, id: str) -> bool:
        """Check ID"""
        try:
            test = storage.all()[cls+'.'+id]
            return True if test else False
        except KeyError:
            return False

    @staticmethod
    def check_args(*args):
        """Check Args"""
        for arg in args:
            if not arg["val"]:
                print(arg["msg"])
                return False
        return True

    def check(self, cls: str, lvl=0, id: str | None = None) -> bool | None:
        """Command Check Handler"""
        if not cls:
            print("** class name missing **")
        elif not self.check_cls(cls):
            print("** class doesn't exist **")
        elif lvl > 0 and not id:
            print("** instance id missing **")
        elif lvl > 0 and not self.check_id(cls, id):
            print("** no instance found **")
        else:
            return True

    def emptyline(self) -> None:
        """Handles empty lines by doing nothing\n"""

    def do_EOF(self, line: str) -> bool:
        """Handles EOF (Ctrl+D) to exit the shell\n"""
        return True

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line: str) -> None:
        """Create command"""
        (class_name, ) = self.cmd_options(line, 1)
        if self.check(class_name):
            instance = globals()[class_name]()
            instance.save()
            print(instance.id)

    def do_show(self, line: str) -> None:
        """Show command"""
        (class_name, id,) = self.cmd_options(line, 2)
        if self.check(class_name, 1, id):
            obj = storage.all()[f"{class_name}.{id}"]
            instance = globals()[class_name](**obj)
            print(instance)

    def do_destroy(self, line: str) -> None:
        """Destroy command"""
        (class_name, id,) = self.cmd_options(line, 2)
        if self.check(class_name, 1, id):
            storage.delete(f"{class_name}.{id}")
            storage.save()

    def do_all(self, line: str) -> None:
        """List all instances of a class"""
        (class_name,) = self.cmd_options(line, 1)
        if not class_name:
            print(storage.all())
        elif self.check(class_name):
            print(storage.all_cls(class_name))

    def do_update(self, line: str) -> None:
        """Update an attribute value for an object."""
        (class_name, id, attr, value) = self.cmd_options(line, 4)
        args = [{"val": attr, "msg": "** attribute name missing **"},
                {"val": value, "msg": "** value missing **"}]
        if self.check(class_name, 2, id) and self.check_args(*args):
            obj = storage.all()[f"{class_name}.{id}"]
            instance = globals()[class_name](**obj)
            setattr(instance, attr, type(attr)(value.strip('"')))
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
