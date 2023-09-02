#!/usr/bin/python3
import cmd
from Models.base_model import BaseModel
from Models import storage
from Models.engine.file_storage import FileStorage
from Models.user import User
from Models.amenity import Amenity
from Models.city import City
from Models.place import Place
from Models.review import Review
from Models.state import State
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

    def do_create(self, args):
        '''creates an instance of a class
        saves the instance and prints id'''
        new_args = args.split(' ')
        class_name = new_args[0]
        if len(class_name) == 0:
            print("** Class name missing")
        else:
            if class_name not in HBNBCommand.classes.keys():
                print('** Class not found')
            else:
                '''create a new instance of the class'''
                obj = HBNBCommand.classes[class_name]()
                '''parse the parameters in the form of key=value'''

                params = {}

                for param in new_args[1:]:
                    key_value = param.split('=')
                    if len(key_value) == 2:
                        key, value = key_value
                        params[key] = value
                    else:
                        print('**invalid syntax')
                '''set the instance attributes with the newly parse parameters'''

                for key, value in params.items():
                    setattr(obj, key, value)
                '''save the object and print its id'''
                obj.save()
                print(obj.id)
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