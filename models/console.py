#!/usr/bin/python3

""" The entry point of the command interpreter """

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ Class that contains the entry point of the command interpreter"""
    #prompt = '(hbnb)'

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        sys.exit(1)
    #shorcut
    quit = do_quit
    EOF = do_EOF

if __name__ == '__main__':
    HBNBCommand().cmdloop()