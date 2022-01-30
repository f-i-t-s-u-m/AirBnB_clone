#!/usr/bin/python3
""" filestorage python file """

import json, os

class FileStorage:
    """ python class"""
    __file_path = 'data.json'
    __objects = {}

    def __init__(self):
        """ class init """
        pass

    def all(self):
        """ return objects"""
        return self.__objects

    def new(self, obj):
        """ sets to __objs"""
        self.__objects = {type(obj).__name__+"."+ obj.id : obj}

    def save(self):
        """ serialize _object to json"""
        objFile = {}
        try:
            with open(self.__file_path) as readData:
                    objFile = json.load(readData)
        except FileNotFoundError:
            pass
        with open(self.__file_path, "w") as data:
            obj = {k: v.to_dict() for k, v in self.__objects.items()}
            obj.update(objFile)
            json.dump(obj, data)

    def classes(self):
        """
        load classes from 
        """
        from models.base_model import BaseModel
        classData = {
                "BaseModel":BaseModel
                }
        return classData

    def reload(self):
        """ load or deserilizes json file to _objs"""
        from  models.base_model import BaseModel
        try:
            with open(self.__file_path) as jsonfile:
                obj = json.load(jsonfile)
                obj = {k: self.classes()[v['__class__']](**v) for k, v in obj.items()}
                self.__objects = obj

        except FileNotFoundError:
            pass



