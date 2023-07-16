#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
"""A class that marks the entry point to the CLI"""

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB: '

    classes  = {'BaseModel': BaseModel}

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
