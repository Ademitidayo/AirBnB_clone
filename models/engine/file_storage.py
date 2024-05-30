#!/usr/bin/python3
"""defines the file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        obj_class = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_class, obj.id)] = obj

    def get(self, key):
        """Retrieve an instance based on the given key."""
        return self.__objects.get(key)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            serialized_data = {}
            for key, obj in self.__objects.items():
                if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                    serialized_data[key] = obj.to_dict()
            json.dump(serialized_data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
