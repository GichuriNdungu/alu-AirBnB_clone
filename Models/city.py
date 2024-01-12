#!/usr/bin/python3
from Models.base_model import BaseModel
'''user class that inherits from BaseModel'''
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City (BaseModel()):
    __tablename__ = 'Cities'
    name = Column(String(128),nullable=False)
    state_id = Column(String(60),ForeignKey ('states.id'),nullable=False,)
