#!/usr/bin/python3
from Models.base_model import BaseModel
'''user class that inherits from BaseModel'''

class User (BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
