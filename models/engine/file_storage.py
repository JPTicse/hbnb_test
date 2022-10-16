#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
import os
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class FileStorage:
    """File Storage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Function that add elements in the dictionary 
            sets in __objects the obj with key <obj class name>.id"""
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, values in new_object_dict.items():
                #self.__objects[keys] = values
                self.__objects[keys] = eval(values['__class__'])(**values)
           