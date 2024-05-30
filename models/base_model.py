#!/usr/bin/python3

"""defines the base model of the project"""
import models
import uuid
from datetime import datetime

class BaseModel:
    """Represents the basemodel for the AirBNB project"""
    def __init__(self, *args, **kwargs):
        # initialize a new base model
        # args: any
        # kwargs: dictionary of key/value pairs representing attributes

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """represents the string representation of the base model"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        a_dict = self.__dict__.copy()
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        a_dict["__class__"] = self.__class__.__name__
        return a_dict
