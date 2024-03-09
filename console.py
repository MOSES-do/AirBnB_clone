#!/usr/bin/env python3

""" Command Interpreter """
import cmd
import os
import json
import re
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ AirBnB Command Interpreter """
    prompt = "(hbnb) "

    def do_create(self, line):
        """ create instance of a BaseModel """
        if line == "":
            print("** class name missing **")
        elif line == "BaseModel":
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ prints obj  of a BaseModel """
        p = re.compile(r'^[\da-fA-F]{8}(-[\da-fA-F]{4}){3}-[\da-fA-F]{12}$')
        pattern1 = re.compile(r'^[A-za-z]+$')
        if line != "":
            args = line.split()
            if (args and len(args) == 1):
                idMatch = re.match(p, args[0])
                clMatch = re.match(pattern1, args[0])
                if idMatch:
                    print("** class name is missing **")
                elif clMatch and args[0] != "BaseModel":
                    print("** class doesn't exist **")
                elif clMatch and args[0] == "BaseModel":
                    print("** instance id missing **")
                elif (args and len(args) == 2):
                    klas, id = args
                    """print(id)"""
                    if os.path.exists("file.json"):
                        with open("file.json", "r") as f:
                            json_str = json.load(f)
                            """print(json_str)"""
                            for key, value in json_str.items():
                                id_value = value.get('id')
                                if id_value == id:
                                    obj = BaseModel(**value)
                                    print(f"{obj}")
                                else:
                                    """comparism doesn't work yet
                                    print("** no instance found **")
                                    print(id, id_value)"""
                                    pass
                    else:
                        pass
            elif (args and len(args) > 2):
                print("Invalid input. Usage: show  <class> <id>")
        else:
            print("** class name is missing **")

    def do_all(self, line):
        """ print all instances of BaseModel """
        if os.path.exists("file.json"):
            with open("file.json", "r") as f:
                json_str = json.load(f)
            if (line != ""):
                args = line.split()
                if (args[0] != "BaseModel"):
                    print("** class name doesn't exist **")
                for key, value in json_str.items():
                    id_value = value.get('__class__')
                    if id_value == args[0]:
                        obj = BaseModel(**value)
                        """formatted output still missing double quote"""
                        print(f"[{obj}]")
            elif (line == ""):
                for key, value in json_str.items():
                    obj = BaseModel(**value)
                    """formatted output still missing double quote"""
                    print(f"[{obj}]")
        else:
            pass

    def do_quit(self, line):
        """ Quit AirBnB terminal by typing 'quit' """
        return True

    def do_EOF(self, line):
        """ Exit terminal by pressing 'CTRL + D' """
        print()
        return True

    def default(self, line):
        """ Prints a custom prompt with empty line, if
            no command is passed to terminal
        """
        print(f"Unknown command: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
