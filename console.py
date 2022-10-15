#!/usr/bin/python3

""" The entry point of the command interpreter """

import cmd
import sys

from  models.base_model import BaseModel
from models import storage


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
            return
        elif name_class != 'BaseModel':
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id.
        """
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing ** ")
            return

        elif list_arg[0] != 'BaseModel':
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                print(dict_all_obj[string])

    def do_destroy(self, class_Id):
        """Deletes an instance based on the class name and id 
        (save the change into the JSON file). 
        Ex: $ destroy BaseModel 1234-1234-1234"""

        list_arg = class_Id.split(" ")

        if not class_Id:
            print("**class name missing**")
            return

        elif list_arg[0] != 'BaseModel':
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                del(dict_all_obj[string])
                storage.save()
            
    def do_all(self, newclass):
        """Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all.
        * The printed result must be a list of strings
        * If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ all MyModel)"""

        list_str = []
        obj_str = ""

        if not newclass:
            print("class doesn't exist")
            return
        else:
            #return print('[{}]'.format(str(dict_all_obj)))
            dict_all_obj = storage.all()
            for key, value in dict_all_obj.items():
                obj_str = str(value)
                list_str.append(obj_str)
                print(list_str)

    def do_update(self, class_name, id, attr_name, attr_value):
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()