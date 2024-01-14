#!/usr/bin/python3
"""File Storage Model"""

import json
from os import path

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Storage class for storing data in json file"""

    __file_path = "file.json"
    __objects = dict()
    __classes = {'BaseModel': BaseModel, 'User': User,
                 'State': State, 'Place': Place,
                 'City': City, 'Amenity': Amenity, 'Review': Review}

    def all(self):
        """Get all stored objects"""
        return self.__objects

    def all_cls(self, cls: str):
        """Get all instances of a specific class from the store"""
        result = dict()
        for key in self.__objects:
            if key.split('.')[0] == cls:
                result[key] = self.__objects[key]
        return result

    def new(self, obj):
        """Add new obj to storage"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def delete(self, key):
        """Delete object by its key (Class.ID)"""
        if key in self.__objects:
            del self.__objects[key]

    def save(self):
        """Save current state of the object list into a file"""
        jsonDict = dict()
        for key, val in self.__objects.items():
            jsonDict[key] = val.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(jsonDict, file)

    def reload(self):
        """Reload the object from the storage"""
        if self.__file_path and path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                jsonDict = json.load(file)
                for (key, value) in jsonDict.items():
                    self.__objects[key] = self.__classes[key.split('.')[
                        0]](**value)
