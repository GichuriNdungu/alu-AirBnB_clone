#!/usr/bin/python3
from Models import storage
from Models.base_model import BaseModel

all_objs = storage.all()
print(all_objs)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
