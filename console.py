#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
"""A class that marks the entry point to the CLI"""

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB: '

    classes  = {'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'Amenity': Amenity,
                'City': City,
                'Review': Review,
                'Place': Place}

    def do_create(self, class_name):
        '''creates an instance of a class
        saves the instance and prints id'''
        if len(class_name) == 0:
            print("** Class name missing")
        elif class_name in HBNBCommand.classes.keys():
            obj = HBNBCommand.classes[class_name]()
            obj.save()
            print(obj.id)
        else:
            print('** Class not found')
    def do_show(self, cls_id):

        '''return str rep of obj
        params; class_name, obj id'''
        args = cls_id.split()
        if len(args) == 0:
            print("** Class name missing")
        elif len(args) == 1:
            print('** Instance id is missing')
        else:
            cls = args[0]
            obj_id = args[1]
            key = cls + '.' + obj_id
            if cls not in HBNBCommand.classes.keys():
                print("** Class doesn't exist")
            else:
                try:
                    all_objs = storage.all()
                    obj_ids = all_objs.keys()
                    obj = all_objs[key]
                    print(obj)
                except Exception as e:
                    print("** No instance found")
    def do_destroy(self, cls_id):

        '''Destroy object by given parameters'''
        args = cls_id.split()
        if len(args) == 0:
            print("** Class name missing")
        elif len(args) == 1:
            print('** Instance id is missing')
        else:
            cls = args[0]
            obj_id = args[1]
            key = cls + '.' + obj_id
            if cls not in HBNBCommand.classes.keys():
                print("** Class doesn't exist")
            else:
                try:
                    all_objs = storage.all()
                    del all_objs[key]
                    storage.save()
                except Exception as e:
                    print("** No instance found")
    def do_all(self, args):
        '''Prints a list of all objects
        params; class_name
        return; str instance of all objs'''
        if len(args) == 0:
            all_objs = storage.all()
            obj_list = []
            for key, value in all_objs.items():
                obj = str(value)
                obj_list.append(obj)
                print(obj_list)
        else: 
            all_objs = storage.all()
            obj_list = []
            for key, value in all_objs.items():
                cls_name = key.split('.')[0]
                if cls_name == args:
                    obj_list.append(str(value))
                    print(obj_list)
    def do_update(self, updates):
        '''updates instance with new attributes'''
        args = updates.split()
        if len(args) == 0:
            print("** Class name missing")
        elif len(args) == 1:
            print('** Instance id is missing')
        elif len(args) == 2:
            print('** attribute name missing')
        elif len(args) == 3:
            print('** Value missing')
        else:
            attribute_name = args[2]
            value = args[3]
            cls_name = args[0]
            ins_id = args[1]    
            key = cls_name + '.' + ins_id
            if cls_name not in HBNBCommand.classes.keys():
                print("** Class does not exists **")
            elif key not in storage.all().keys():
                print("** no instance found **")
            else:
                all_objs = storage.all()
                obj = (all_objs[key])
                setattr(obj, attribute_name, value)
                storage.save()
    def do_quit(self, arg):
        '''exits the program'''
        print('''Exiting...''')
        return True
    def do_EOF(self, arg):
        '''Exits the program'''
        print('Exiting...')
        return True
    def do_help(self, arg):
        '''Display information about commands'''
        if arg:
            '''Display information for a specific command'''
            self.onecmd(f"Help, {arg}")
        else:
            '''display general information about commands'''
            for command in self.get_names():
                if command.startswith('do_'):
                    cmd_name = command[3:]
                    doc = getattr(self, command).__doc__
                    print(f'{cmd_name}:{doc}')
    def emptyline(self):
        '''do nothing when empty line is entered'''

        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()