#!/usr/bin/python3
"""File Storage Model"""

import json
from os import path


class FileStorage():
    """Storage class for storing data in json file"""

    __file_path = "file.json"
    __objects = dict()

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
        self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def delete(self, key):
        """Delete object by its key (Class.ID)"""
        if key in self.__objects:
            del self.__objects[key]

    def save(self):
        """Save current state of the object list into a file"""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Reload the object from the storage"""
        if self.__file_path and path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
