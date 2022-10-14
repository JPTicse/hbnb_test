#!/usr/bin/python3

""" The entry point of the command interpreter """

import cmd
import sys

from  models.base_model import BaseModel


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
        """ Exit the program quit"""
        sys.exit(1)
        
    def emptyline(self):
        """ Empty line"""
        pass

    def do_create(self, name_class):
        """Create a new instance of Basemodel, save it (to JSON file) 
           and prints the id."""
        if not name_class:
            print("**class name missing**")
        elif name_class != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, name_class, id):
        """Prints the string representation of an instance based on the
        class name and id. (Ex: $ show BaseModel 1234-1234-1234)"""
        if not name_class:
            print("**class name missing**")
        elif name_class != 'BaseModel':
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()