#!/usr/bin/python3
"""Storage Class"""

import json
from os import path


class FileStorage():
    """Storage class for storing data in json file"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Get all stored objects"""
        return self.__objects

    def new(self, obj):
        """Add new obj to storage"""
        self.__objects[obj['__class__'] + '.' + obj['id']] = obj

    def save(self):
        """Save current state of the object list into a file"""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Reload the object from the storage"""
        if self.__file_path and path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
