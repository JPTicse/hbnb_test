#!/usr/bin/python3

""" The entry point of the command interpreter """

import cmd
import sys

from  models.base_model import BaseModel
from models import storage
list_class = {"BaseModel": BaseModel}

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
            
    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id.
        """
        list_arg = args.split(" ")

        if len(args) == 0:
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
        dict_all_obj = storage.all()
        list_arg = newclass.split(" ")
        list_str = []
        obj_str = ""
        if len(newclass) == 0:
            for key, value in dict_all_obj.items():
                list_str.append(str(value))
                print(list_str)
                return
        if not list_arg[0] in list_class:
            print("class doesn't exist")
            return
        else:
            for key, value in dict_all_obj.items():
                name_class = key.split(".")
                if name_class[0] == list_arg[0]:
                    list_str.append(str(value))
                    print(list_str)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or 
        updating attribute (save the change into the JSON file). 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""   
        list_arg = args.split(" ")

        if not args:
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
                return
            elif len(list_arg) < 3:
                print("** attribute name missing **")
                return
            elif len(list_arg) < 4:
                print("** value missing **")
                return
            else:
                list_param = ["id", "created_at", "updated_at"]
                if not list_arg[2] in list_param:
                    dict_all_obj = storage.all()
                    string = f'{list_arg[0]}.{list_arg[1]}'
                    for key, value in dict_all_obj.items():
                        if key == string:
                            dict_value = value.__dict__
                            dict_value[list_arg[2]] = list_arg[3]
                            value.save()
                else:
                    print("Cant’ be updated")

if __name__ == '__main__':
    HBNBCommand().cmdloop()