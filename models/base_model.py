#!/usr/bin/python3
""" base model file """


import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """ class of base model"""
   
    def __init__(self, *args, **kwargs):
        """ init the class"""
        if kwargs is not None and  kwargs != {}:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.strptime(str(v), 
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ return str version """
        return str("[{}] ({}) {}".format(BaseModel.__name__, 
            self.id, self.__dict__));

    def save(self):
        """ save data"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """ return the dict version of the app"""
        dictm = self.__dict__.copy()
        dictm['__class__'] = type(self).__name__
        dictm['created_at'] = dictm['created_at'].isoformat()
        dictm['updated_at'] = dictm['updated_at'].isoformat()
        return dictm
