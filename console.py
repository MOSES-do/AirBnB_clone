#!/usr/bin/python3

""" Command Interpreter """
import cmd
import os
import json
import uuid
import re
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ AirBnB Command Interpreter """
    prompt = "(hbnb) "
    file_path = "file.json"

    def precmd(self, line):
        """modify cmd argument patterns"""
        re1 = r'^[A-za-z]+\.[A-za-z]+\([a-fA-F0-9-]+\)$'
        re2 = r'^[a-zA-Z]+\.[a-zA-Z]+\(.*\)$'
        re3 = r'[a-zA-Z]+\.[a-zA-Z]+\("([^"]+)"\)'
        lineMatch = re.match(re1, line)
        lineMatch1 = re.match(re2, line)
        lineMatch2 = re.match(re3, line)

        if lineMatch or lineMatch2:
            c = line.replace(".", " ").replace("(", " ").replace(")", "")
            command = c.split(" ")
            line = f"{command[1]} {command[0]} {command[2]}"
        elif lineMatch1:
            c = line.replace(".", " ").replace("(", "").replace(")", "")
            command = c.split(" ")
            line = f"{command[1]} {command[0]}"

        return cmd.Cmd.precmd(self, line)

    def checkGlobalClass(self, cls):
        """ method checks existence of classes globally """
        pattern1 = re.compile(r'^[A-za-z]+$')
        argMatch = re.match(pattern1, cls)
        class_name = ""
        if (argMatch):
            try:
                model_cls = globals()[cls]
                str_cls = f"{model_cls}"
                class_name = str_cls.split('.')[-1].strip(">'")
            except KeyError:
                print("** class doesn't exist **")
            return class_name

    def do_create(self, line):
        """ create instance of a BaseModel """
        if line == "":
            print("** class name missing **")
            return

        try:
            model_cls = globals()[line]
            cls_model = self.checkGlobalClass(line)
            new_instance_cls = eval(f'{cls_model}()')
            new_instance = new_instance_cls
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")
            return

    def call_show(self, id, cls):
        """ method calls 'show' """
        if os.path.exists(HBNBCommand.file_path):
            with open(HBNBCommand.file_path, "r") as f:
                json_str = json.load(f)
                id_val = ""

                for key, value in json_str.items():
                    id_value = value.get('id')
                    id_cls = value.get('__class__')
                    if id == id_value and cls == id_cls:
                        id_val = id_value
                        cls = globals()[id_cls]
                        py = cls(**value)
                        print(py)
                if (id != id_val):
                    print("** no instance found **")
        else:
            pass

    def do_show(self, line):
        """ prints obj  of a BaseModel """
        p = re.compile(r'^[\da-fA-F]{8}(-[\da-fA-F]{4}){3}-[\da-fA-F]{12}$')
        pattern1 = re.compile(r'^[A-za-z]+$')
        if line != "":
            args = line.split()
            class_name = self.checkGlobalClass(args[0])

            if (args and len(args) == 1):
                idMatch = re.match(p, args[0])
                clMatch = re.match(pattern1, args[0])
                if idMatch:
                    print("** class name is missing **")
                elif (clMatch and args[0] == class_name):
                    print("** instance id missing **")
            elif (args and len(args) == 2):
                klas, id = args
                if class_name == klas:
                    self.call_show(id, klas)
            elif (args and len(args) > 2):
                print("Invalid input. Usage: show  <class> <id>")
        else:
            print("** class name missing **")

    def do_count(self, line):
        if line != "":
            class_name = self.checkGlobalClass(line)
            with open(HBNBCommand.file_path, "r") as f:
                json_str = json.load(f)
                count = 0
                for key, value in json_str.items():
                    cls_name = value.get('__class__')
                    if cls_name == line:
                        count += 1
                print(count)
        else:
            print("** class name missing **")

    def do_all(self, line):
        """ print all instances of BaseModel """
        if os.path.exists(HBNBCommand.file_path):
            with open(HBNBCommand.file_path, "r") as f:
                json_str = json.load(f)
            if (line != ""):
                args = line.split()
                class_name = self.checkGlobalClass(args[0])
                for key, value in json_str.items():
                    id_value = value.get('__class__')
                    if id_value == args[0]:
                        cls = globals()[id_value]
                        result = cls(**value)
                if (class_name == args[0]):
                    print(result)
            elif (line == ""):
                for key, value in json_str.items():
                    id_value = value.get('__class__')
                    cls = globals()[id_value]
                    result = cls(**value)
                    print(result)
        else:
            pass

    def delete(self, id):
        """ method powers the delete functionality
            and is called from do_show method
        """
        if os.path.exists("file.json"):
            with open("file.json", "r") as f:
                json_str = json.load(f)
                delId = ""
                for key, value in json_str.items():
                    entryId = value.get('id')
                    entryClass = value.get('__class__')
                    if entryId == id:
                        delId = f"{entryClass}.{entryId}"
                if delId in json_str:
                    del json_str[delId]
                else:
                    print("** no instance found **")
                with open("file.json", 'w') as file:
                    json.dump(json_str, file, indent=4)
        else:
            pass

    def do_destroy(self, ids):
        """ Deletes an obj/instance based on its id"""
        p = re.compile(r'^[\da-fA-F]{8}(-[\da-fA-F]{4}){3}-[\da-fA-F]{12}$')
        pattern1 = re.compile(r'^[A-za-z]+$')
        if ids != "":
            args = ids.split()
            class_name = self.checkGlobalClass(args[0])
            if (args and len(args) == 1):
                idMatch = re.match(p, args[0])
                clMatch = re.match(pattern1, args[0])
                if idMatch:
                    print("** class name is missing **")
                elif (clMatch and args[0] != class_name):
                    print("** class doesn't exist **")
                elif (clMatch and args[0] == class_name):
                    print("** instance id missing **")
            elif (args and len(args) == 2):
                klas, id = args
                """delete method called"""
                if class_name == args[0]:
                    self.delete(id)
            elif (args and len(args) > 2):
                print("Invalid input. Usage: show  <class> <id>")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """Update user attributes"""

        arg = arg.split()

        if len(arg) < 1:
            print("** class name missing **")
            return
        class_name = arg[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]
        key = class_name + '.' + instance_id
        every_instance = storage.all()

        if key not in every_instance:
            print("** no instance found **")
            return

        instance = every_instance[key]

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        kiy = arg[2]

        if len(arg) < 4:
            print("** value missing **")
            return

        attr_val = arg[3]

        if len(arg) > 4:
            return

        if hasattr(instance, kiy):
            if kiy == "id" or kiy == "created_at" or kiy == "updated_at":
                return
            attr_val = type(getattr(instance, kiy))(attr_val)
            try:
                setattr(instance, kiy, attr_val)
                storage.save()
            except AttributeError:
                pass
            except ValueError:
                pass

    def do_quit(self, line):
        """ Quit AirBnB terminal by typing 'quit' """
        return True

    def do_EOF(self, line):
        """ Exit terminal by pressing 'CTRL + D' """
        print()
        return True

    def emptyline(self):
        """ Prints an Emptyline """
        pass

    def default(self, line):
        """ Prints a custom prompt with empty line, if
            no command is passed to terminal
        """
        print(f"Unknown command: {line}")

    def help_EOF(self):
        """ Display information for the EOF command """
        pass

    def help_help(self):
        """ Display information for the help command """
        pass

    def help_quit(self):
        """ Display informatin for the quit command """
        print("Quit is a command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
