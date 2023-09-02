#!/usr/bin/python3
from Models.base_model import BaseModel
'''user class that inherits from BaseModel'''

class Review (BaseModel):
    place_id = ''
    user_id = ''
    text = ''