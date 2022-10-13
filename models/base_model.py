#!/usr/bin/python3
""" Module main base_model.py"""

from curses import keyname
import uuid
from datetime import datetime
formato = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize data"""
        if len(kwargs) > 0:
            for key,value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, formato)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.save()

    def __str__(self):
        """Function that returns str representation"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Method to update updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary with all values"""
        dict_temp = self.__dict__.copy()
        dict_temp["__class__"] = self.__class__.__name__
        dict_temp["created_at"] = self.created_at.isoformat()
        dict_temp["updated_at"] = self.updated_at.isoformat()
        return dict_temp
