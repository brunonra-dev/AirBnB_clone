#!/usr/bin/python3
"""
module that defines a FileStorage class
"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """ class that  that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    __classes = {'BaseModel': BaseModel}

    @classmethod
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    @classmethod
    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    @classmethod
    def save(self):
        """ serializes __objects to the
        JSON file (path: __file_path) """
        tmp = {}
        for k, v in self.__objects.items():
            tmp[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(tmp, f)

    @classmethod
    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.isfile(self.__file_path) is False:
            return

        with open(self.__file_path, encoding="utf-8") as f:
            des = json.load(f)
            for k, v in des.items():
                cls = v['__class__']
                self.__objects[k] = self.__classes[cls](**v)
