#!/usr/bin/python3
""" filestorage python file """

import json


class FileStorage:
    """ python class"""
    __file_path = 'data.json'
    __objects = {}

    def __init__(self):
        """ class init """
        pass

    def all(self):
        """ return objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets to __objs"""
        FileStorage.__objects = {type(obj).__name__ + "." + obj.id: obj}

    def save(FileStorage):
        """ serialize _object to json"""
        objFile = {}
        try:
            with open(FileStorage.__file_path) as readData:
                objFile = json.load(readData)
        except FileNotFoundError:
            pass
        with open(FileStorage.__file_path, "w") as data:
            obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            obj.update(objFile)
            json.dump(obj, data)

    def classes(self):
        """
        load classes from
        """
        from models.base_model import BaseModel
        classData = {
                "BaseModel": BaseModel
                }
        return classData

    def reload(self):
        """ load or deserilizes json file to _objs"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path) as jsonfile:
                obj = json.load(jsonfile)
                obj = {k: self.classes()[v['__class__']](**v)
                        for k, v in obj.items()}
                FileStorage.__objects = obj

        except FileNotFoundError:
            pass
