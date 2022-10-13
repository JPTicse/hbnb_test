#!/usr/bin/python3
""" Module main base_model.py"""


import uuid
class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = ""
        self.updated_at = ""

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__, self.id, self.__dict__)

    def save(self):
        self.updated_at = ""

    def to_dict(self):
        return self.__dict__

    
