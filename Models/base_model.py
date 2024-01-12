#!/usr/bin/python3

''' class BaseModel:'''

import uuid
from datetime import datetime
from Models import storage
from Models.engine.file_storage import FileStorage
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime


Base = declarative_base()
class BaseModel():
    """Defines all common attributes/methods for other classes."""
    __tablename__ = 'Base_Model'
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(
                        value, tform)
                if key == "updated_at":
                    value = datetime.strptime(
                    value, tform)
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, value)
            if key == "__class__":
                del kwargs["__class__"]
            self.__dict__.update(kwargs)
        
    def __str__(self):
        ''' string representation of object'''
        name = type(self).__name__
        number = self.id
        dictionary = self.__dict__
        return f'[{name}] ({number}) {dictionary}'

    def save(self):
        ''' update the date of module update to current date'''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        ''' append basemodel with classname'''
        dictionary = self.__dict__.copy()
        if '_sa_instance_state' in dictionary.keys():
            del(dictionary['_sa_instance_state'])
        name = type(self).__name__
        dictionary["__class__"] = name
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if hasattr(self, '__sa_instance_state'):
            del dictionary['_sa_instance_state']

        return dictionary
    def delete(self):
        #delete the current instance from storage
        storage.delete(self)

