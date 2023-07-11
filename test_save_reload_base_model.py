#!/usr/bin/python3
from Models import storage
from Models.base_model import BaseModel

all_objs = storage.all()
print("---Reloaded Objects---")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("---create new object---")

my_model = BaseModel()
my_model.name = ("first_model")
my_model.number = 89
my_model.save()
print(my_model)
