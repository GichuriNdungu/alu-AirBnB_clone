#!/usr/bin/python3

''' class BaseModel:'''

import uuid
from datetime import datetime
from Models import storage
from Models.engine.file_storage import FileStorage
class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], tform)
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], tform)
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)
        storage.new(self)
    def __str__(self):
        ''' string representation of object'''
        name = type(self).__name__
        number = self.id
        dictionary = self.__dict__
        return f'[{name}] ({number}) {dictionary}'

    def save(self):
        ''' update the date of module update to current date'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' append basemodel with classname'''
        dictionary = self.__dict__.copy()
        name = type(self).__name__
        dictionary["__class__"] = name
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary