#!/usr/bin/python3
from Models.base_model import BaseModel
from Models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
'''user class that inherits from BaseModel'''

class State (BaseModel, Base):
    __tablename__ = states
    name = Column(String(128),nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan' )
