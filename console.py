#!/usr/bin/python3
import cmd
"""A class that marks the entry point to the CLI"""

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB: '

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
