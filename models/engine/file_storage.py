#!/usr/bin/python3
"""
module that defines a FileStorage class
"""
import json


class FileStorage:
    """ class that  that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        id_o = obj.id
        class_name = self.__class__.__name__
        self.__objects[class_name + "." + id_o] = obj
        
    @staticmethod
    def to_json(obj):
        """ returns objects in json format """
        if obj is None:
            return "[]"
        return json.dumps(obj)

    @staticmethod
    def from_json(obj):
        """ returns str from json format """
        if obj is None:
            return {}
        return json.loads(obj)

    def save(self):
        """ serializes __objects to the
        JSON file (path: __file_path) """
        serialized = {}
        for k, v in self.__objects.items():
            serialized[k] = json.dump(v)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(serialized)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if not self.__file_path:
            return
        with open(self.__file_path, encoding="utf-8") as f:
            deserialized = json.load(f)
        for k, v in deserialized.items():
            self.__objects[k] = v