#!/usr/bin/python3
"""Console Interpreter"""

import cmd
from re import Pattern, compile, search
from ast import literal_eval

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB Command Shell"""

    prompt = "(hbnb) "

    __all_re = compile(r"(.*?).all\( *\)$")
    __count_re = compile(r"(.*?).count\( *\)$")
    __show_re = compile(r"(.*?).show\( *(.*?) *\)$")
    __destroy_re = compile(r"(.*?).destroy\( *(.*?) *\)$")
    __update_re = compile(
        r"(.*?).update\( *(.*?) *, *(.*?) *, *(.*?) *\)$")
    __update_obj_re = compile(
        r"(.*?).update\( *(.*?) *, *({.*?}) *\)$")
    __classes = {'BaseModel': BaseModel, 'User': User,
                 'State': State, 'Place': Place,
                 'City': City, 'Amenity': Amenity, 'Review': Review}

    @staticmethod
    def handle_quote(*args):
        dquote_re = compile(r"^\"(.*?)\"$")
        squote_re = compile(r"^'(.*?)'$")
        result = []
        for arg in args:
            if arg and search(dquote_re, arg):
                result.append(dquote_re.findall(arg)[0])
            elif arg and search(squote_re, arg):
                result.append(squote_re.findall(arg)[0])
            else:
                result.append(arg)
        return result

    @staticmethod
    def check_id(cls: str, id: str):
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

    def cmd_options(self, line: str, num: int):
        """Return the options for a command line."""
        options = [item for item in line.split(" ") if item]
        options = [options[i] if i < len(
            options) else None for i in range(num)]
        return self.handle_quote(*options)

    def check(self, cls: str, lvl=0, id: str = None):
        """Command Check Handler"""
        if not cls:
            print("** class name missing **")
        elif cls not in self.__classes:
            print("** class doesn't exist **")
        elif lvl > 0 and not id:
            print("** instance id missing **")
        elif lvl > 0 and not self.check_id(cls, id):
            print("** no instance found **")
        else:
            return True

    def custom_cmd_options(self, regex: Pattern[str], line):
        options = regex.findall(line)
        return self.handle_quote(*(
            options if type(options[0]) == str else options[0]))

    def update(self, class_name: str, id: str, attr: str, value: str):
        """Update Attribute Value"""
        args = [{"val": attr, "msg": "** attribute name missing **"},
                {"val": value, "msg": "** value missing **"}]
        if self.check(class_name, 2, id) and self.check_args(*args):
            obj = storage.all()[f"{class_name}.{id}"]
            instance = self.__classes[class_name](**obj)
            setattr(instance, attr, type(
                getattr(instance, attr))(value))
            instance.save()

    def update_obj(self, class_name: str, id: str, dic: str):
        args = [{"val": dic, "msg": "** update obj missing **"}]
        if self.check(class_name, 2, id) and self.check_args(*args):
            obj = storage.all()[f"{class_name}.{id}"]
            instance = self.__classes[class_name](**obj)
            dic = literal_eval(dic)
            for key in dic:
                setattr(instance, key, type(getattr(instance, key))(dic[key]))
            instance.save()

    def all(self, class_name):
        """Return All Instances of a Class"""
        if not class_name:
            print(storage.all())
        elif self.check(class_name):
            print(storage.all_cls(class_name))

    def count(self, class_name):
        """Count Number of Instances of a Class"""
        if not class_name:
            print(len(storage.all()))
        elif self.check(class_name):
            print(len(storage.all_cls(class_name)))

    def destroy(self, class_name, id):
        """Destroy an Object by its ID"""
        if self.check(class_name, 1, id):
            storage.delete(f"{class_name}.{id}")
            storage.save()

    def show(self, class_name, id):
        """Show the Details of an Object"""
        if self.check(class_name, 1, id):
            obj = storage.all()[f"{class_name}.{id}"]
            instance = self.__classes[class_name](**obj)
            print(instance)

    def create(self, class_name):
        """Create New Object from Class Name"""
        if self.check(class_name):
            instance = self.__classes[class_name]()
            instance.save()
            print(instance.id)

    def emptyline(self):
        """Handles empty lines by doing nothing"""
        pass

    def do_EOF(self, line: str):
        """Handles EOF (Ctrl+D) to exit the shell"""
        print("")
        return True

    def do_quit(self, line: str):
        """Quit command to exit the program"""
        return True

    def do_create(self, line: str):
        """Create command"""
        self.create(*self.cmd_options(line, 1))

    def do_show(self, line: str):
        """Show command"""
        self.show(*self.cmd_options(line, 2))

    def do_destroy(self, line: str):
        """Destroy command"""
        self.destroy(*self.cmd_options(line, 2))

    def do_all(self, line: str):
        """List all instances of a class"""
        self.all(*self.cmd_options(line, 1))

    def do_update(self, line: str):
        """Update an attribute value for an object."""
        self.update(*self.cmd_options(line, 4))

    def default(self, line: str):
        """Default handler when no specific handler is found"""

        if (search(self.__all_re, line)):
            self.all(*self.custom_cmd_options(self.__all_re, line))
        elif (search(self.__count_re, line)):
            self.count(*self.custom_cmd_options(self.__count_re, line))
            # self.count(*self.__count_re.findall(line))
        elif (search(self.__show_re, line)):
            self.show(*self.custom_cmd_options(self.__show_re, line))
        elif (search(self.__destroy_re, line)):
            self.destroy(*self.custom_cmd_options(self.__destroy_re, line))
        elif (search(self.__update_re, line)):
            self.update(*self.custom_cmd_options(self.__update_re, line))
        elif (search(self.__update_obj_re, line)):
            self.update_obj(
                *self.custom_cmd_options(self.__update_obj_re, line))
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
