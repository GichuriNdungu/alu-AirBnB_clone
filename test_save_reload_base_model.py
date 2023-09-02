#!/usr/bin/python3
from Models import storage
from Models.base_model import BaseModel
from Models.user import User

First_user = User()
First_user.email = 'n.ndungu@alustudent.com'
First_user.name = 'martin'
print(First_user)