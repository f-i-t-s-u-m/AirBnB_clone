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
        return self.__objects

    def new(self, obj):
        """ sets to __objs"""
        self.__objects = {type(obj).__name__+"."+ obj.to_dict()['id'] : obj.to_dict()}

    def save(self):
        """ serialize _object to json"""
        try:
            with open(self.__file_path) as readData:
                loadedJson = readData.read()
                if loadedJson:
                    self.__objects.update(json.loads(loadedJson))
        except FileNotFoundError:
            pass
        with open(self.__file_path, "w") as data:
                json.dump(json.loads(json.dumps(self.__objects)), data)

    def reload(self):
        """ load or deserilizes json file to _objs"""
        try:
            with open(self.__file_path) as jsonfile:
               self.__objects = json.load(jsonfile)
        except FileNotFoundError:
            pass



