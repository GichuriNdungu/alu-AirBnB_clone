#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""A class that marks the entry point to the CLI"""

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB: '

    

    def do_create(self, class_name):
        classes  = {'BaseModel': BaseModel}
        '''creates an instance of a class
        saves the instance and prints id'''
        if len(class_name) == 0:
            print("** Class name missing")
        elif class_name in classes.keys():
            obj = classes[class_name]()
            obj.save()
            print(obj.id)
        else:
            print('** Class not found')
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
