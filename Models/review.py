#!/usr/bin/python3
from models.base_model import BaseModel
'''user class that inherits from BaseModel'''

class Review (BaseModel):
    place_id = ''
    user_id = ''
    text = ''