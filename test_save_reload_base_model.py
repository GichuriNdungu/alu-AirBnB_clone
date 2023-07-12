#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
print("--reloaded objects--")
all_objs = storage.all()
for obj_id in all_objs:
    obj = all_objs[obj_id]
    print(obj)

print("---create new object---")

my_model = BaseModel()
my_model.name = ("first_model")
my_model.number = 89
my_model.save()
print(my_model)
