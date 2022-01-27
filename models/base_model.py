#!/usr/bin/python3
""" base model file """


import json, uuid, datetime

class BaseModel():
    """ class of base model"""
    name = ""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    
    def __str__(self):
        return str("[{}] ({}) {}".format(BaseModel.__name__, 
            self.id, self.__dict__));

    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        dictm = {}
        dictm['my_number'] = self.my_number
        dictm['name'] = self.name
        dictm['updated_at'] = self.updated_at
        dictm['id'] = self.id
        dictm['created_at'] = self.created_at
        dictm['__class__'] = BaseModel.__name__
        return dictm
