#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel



print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_second_model"
my_model.my_number = 89
my_model.save()
print(my_model)

all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)