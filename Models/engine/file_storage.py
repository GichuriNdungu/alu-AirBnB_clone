#!/usr/bin/python3
''' new class filestorage that stores new objects in a json file'''

import json


class FileStorage:
    ''' class filestorage, serializes object instance.
    The class will also deserialize Json files into instances
     private class attributes'''

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''class constructor'''
        pass

    def all(self):
        ''' return the dictionary rep of objects'''
        return self.__objects

    def new(self, obj):
        ''' input the new object into __objects.'''
        ''' classname.id is the key and obj name is value'''

        cls_name = obj.__class__.__name__
        key = cls_name + '.'+ obj.id
        self.__objects[key] = obj

    def save(self):
        '''serialize new object into __file_path'''
        dictionary = {}
        for obj in self.__objects:
            dictionary[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, "w") as new_file:
            json.dump(dictionary, new_file)
    def reload(self):
        '''deserializes the json file (__file_path) to t
        the __objects dictionary'''
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                dictionary = json.load(f)
                for key, value  in dictionary.items():
                    cls_name = eval(value['__class__'])
                    obj = cls_name(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass