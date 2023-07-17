#!/usr/bin/python3
from models.base_model import BaseModel
'''user class that inherits from BaseModel'''

class User (BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
