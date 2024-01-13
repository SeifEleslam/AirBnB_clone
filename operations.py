#!/usr/bin/python3
"""Ops Model"""
# from models.review import Review
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.state import State
# from models.user import User
# from models.base_model import BaseModel
# from models import storage
# from ast import literal_eval


def cmd_options(line: str, num: int) -> list[str]:
    """Return the options for a command line."""
    options = [item for item in line.split(" ") if item]
    options = [options[i] if i < len(
        options) else None for i in range(num)]
    return options


class Operations():
    """Class for handling operations on the data in the database."""
    # @staticmethod

    # def check_cls(cls: str) -> bool:
    #     """Check Class"""
    #     try:
    #         globals()[cls]
    #         return True
    #     except KeyError:
    #         return False

    # def check_id(cls: str, id: str) -> bool:
    #     """Check ID"""
    #     try:
    #         test = storage.all()[cls+'.'+id]
    #         return True if test else False
    #     except KeyError:
    #         return False

    # def check_args(*args):
    #     """Check Args"""
    #     for arg in args:
    #         if not arg["val"]:
    #             print(arg["msg"])
    #             return False
    #     return True

    # def check(cls: str, lvl=0, id: str | None = None) -> bool | None:
    #     """Command Check Handler"""
    #     if not cls:
    #         print("** class name missing **")
    #     elif not check_cls(cls):
    #         print("** class doesn't exist **")
    #     elif lvl > 0 and not id:
    #         print("** instance id missing **")
    #     elif lvl > 0 and not check_id(cls, id):
    #         print("** no instance found **")
    #     else:
    #         return True

    # def update(class_name: str, id: str, attr: str, value: str):
    #     """Update Attribute Value"""
    #     args = [{"val": attr, "msg": "** attribute name missing **"},
    #             {"val": value, "msg": "** value missing **"}]
    #     if check(class_name, 2, id) and check_args(*args):
    #         obj = storage.all()[f"{class_name}.{id}"]
    #         instance = globals()[class_name](**obj)
    #         setattr(instance, attr, type(
    #             getattr(instance, attr))(value.strip('"')))
    #         instance.save()

    # def update_obj(class_name: str, id: str, dic: str):
    #     args = [{"val": dic, "msg": "** update obj missing **"}]
    #     if check(class_name, 2, id) and check_args(*args):
    #         obj = storage.all()[f"{class_name}.{id}"]
    #         instance = globals()[class_name](**obj)
    #         dic = literal_eval(dic)
    #         for key in dic:
    #             setattr(instance, key, type(getattr(instance, key))(dic[key]))
    #         instance.save()

    # def all(class_name):
    #     """Return All Instances of a Class"""
    #     if not class_name:
    #         print(storage.all())
    #     elif check(class_name):
    #         print(storage.all_cls(class_name))

    # def count(class_name):
    #     """Count Number of Instances of a Class"""
    #     if not class_name:
    #         print(len(storage.all()))
    #     elif check(class_name):
    #         print(len(storage.all_cls(class_name)))

    # def destroy(class_name, id):
    #     """Destroy an Object by its ID"""
    #     if check(class_name, 1, id):
    #         storage.delete(f"{class_name}.{id}")
    #         storage.save()

    # def show(class_name, id):
    #     """Show the Details of an Object"""
    #     if check(class_name, 1, id):
    #         obj = storage.all()[f"{class_name}.{id}"]
    #         instance = globals()[class_name](**obj)
    #         print(instance)

    # def create(class_name):
    #     """Create New Object from Class Name"""
    #     if check(class_name):
    #         instance = globals()[class_name]()
    #         instance.save()
    #         print(instance.id)
