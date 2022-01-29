#!/usr/bin/python3
""" filestorage python file """

import json

class FileStorage():
    """ python class"""
    __file_path = 'data.json'
    __objects = {}


    def all(self):
        """ return objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets to __objs"""
       # FileStorage.__objects = {type(obj).__name__+"."+ obj.id : obj}
        #key = "{}.{}".format(type(obj).__name__, obj.id)
        #FileStorage.__objects[key] = obj
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj 

    def save(self):
        """ serialize _object to json"""
        """  try:
            with open(FileStorage.__file_path) as readData:
                loadedJson = readData.read()
                if loadedJson:
                    FileStorage.__objects.update(json.loads(loadedJson))
        except FileNotFoundError:
            pass
        with open(FileStorage.__file_path, "w") as data:
                json.dump(json.loads(json.dumps(FileStorage.__objects)), data)"""

    def reload(self):
        """ load or deserilizes json file to _objs"""
        try:
            with open(FileStorage.__file_path) as jsonfile:
               #self.__objects = json.loads(jsonfile.read())
               pass
        except FileNotFoundError:
            pass



