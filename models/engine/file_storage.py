#!/usr/bin/python3
"""
module that defines a FileStorage class
"""
import json
from os import path
from collections import namedtuple


class FileStorage:
    """ class that  that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    @classmethod
    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        if obj is not None:
            id_o = obj.id
            class_name = self.__class__.__name__
            self.__objects[class_name + "." + id_o] = obj.__dict__
        
    @staticmethod
    def to_json(obj):
        """ returns objects in json format """
        return json.dumps(obj)

    @staticmethod
    def from_json(obj):
        """ returns str from json format """
        return json.loads(obj)

    @classmethod
    def save(self):
        """ serializes __objects to the
        JSON file (path: __file_path) """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj = FileStorage.__objects.copy()
            for v in obj.values():
                v["created_at"] = str(v["created_at"])
                v["updated_at"] = str(v["updated_at"])
            json.dump(obj, f)
    
    def create(**dict):
        name = dict[id]

    @classmethod
    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.isfile(self.__file_path) is False:
            return {}

        with open(self.__file_path, encoding="utf-8") as f:
            deserialized = json.load(f)
            for k, v in deserialized.items():
                self.__objects[k] = v
