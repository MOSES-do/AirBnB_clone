#!/usr/bin/env python3

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


class HBNBCommand(cmd.Cmd):
    """ AirBnB Command Interpreter """
    prompt = "(hbnb) "
    file_path = "file.json"

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

        try:
            model_cls = globals()[line]
        except KeyError:
            print("** class doesn't exist **")
            return

        new_instance = model_cls()
        new_id = str(uuid.uuid4())
        setattr(new_instance, "id", new_id)

        self.save(new_instance)
        print(new_id)

    def save(self, arg):
        """save instance object to a JSON file"""

        if os.path.isfile(HBNBCommand.file_path):
            with open(HBNBCommand.file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        instance_dict = arg.to_dict()
        value = instance_dict["id"]
        data[arg.__class__.__name__ + "." + value] = instance_dict

        keyValueFormat = instance_dict

        with open(HBNBCommand.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def call_show(self, id):
        """ method calls 'show' """
        if os.path.exists(HBNBCommand.file_path):
            with open(HBNBCommand.file_path, "r") as f:
                json_str = json.load(f)
                id_val = ""
                for key, value in json_str.items():
                    id_value = value.get('id')
                    if id == id_value:
                        id_val = id_value
                        obj = BaseModel(**value)
                        print(obj)
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
                    self.call_show(id)
            elif (args and len(args) > 2):
                print("Invalid input. Usage: show  <class> <id>")
        else:
            print("** class name is missing **")

    def time_convert(self, obj):
        """convert format for timestamps """
        for key, value in obj.items():
            if key.endswith("_at"):
                date_part, time_part = value.split("T")
                y, mth, d = map(int, date_part.split("-"))
                time_parts = time_part.split(":")
                h, m = map(int, time_part[:2])
                second, microsecond = map(int, time_parts[2].split("."))
                dt = datetime(y, mth, d, h, m, second, microsecond)
                fm_dt = (
                    f"datetime.datetime({dt.year}, {dt.month}, {dt.day}, "
                    f"{dt.hour}, {dt.minute}, {dt.second}, {dt.microsecond})"
                )
                obj[key] = fm_dt
                return obj

    def do_all(self, line):
        """ print all instances of BaseModel """
        if os.path.exists(HBNBCommand.file_path):
            with open(HBNBCommand.file_path, "r") as f:
                json_str = json.load(f)
            strs = []
            if (line != ""):
                args = line.split()
                class_name = self.checkGlobalClass(args[0])
                for key, value in json_str.items():
                    id_value = value.get('__class__')
                    if id_value == args[0]:
                        obj1 = value
                        """fn()call to convert "time" to suit req..."""
                        time_c = self.time_convert(obj1)
                        m__name = f"[{obj1['__class__']}]"
                        m__id = "(" + value["id"] + ")"
                        m__attr = str(value)
                        m__instance = f"{m__name} {m__id} {m__attr}"
                        strs.append(m__instance)
                if (class_name == args[0]):
                    result = "[" + ", ".join(strs) + "]"
                    print(result)

            elif (line == ""):
                for key, value in json_str.items():
                    obj1 = value
                    time_c = self.time_convert(obj1)
                    model_name = f"[{obj1['__class__']}]"
                    model_id = "(" + value["id"] + ")"
                    model_attr = str(value)
                    model_instance = f"{model_name} {model_id} {model_attr}"
                    strs.append(model_instance)
                result = "[" + ", ".join(strs) + "]"
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
            print("** class name is missing **")

    def do_update(self, ids):
        """ Updates an obj/instance based on its id"""
        p = re.compile(r'^[\da-fA-F]{8}(-[\da-fA-F]{4}){3}-[\da-fA-F]{12}$')
        attr_v = re.compile(r'^[A-za-z0-9._+*%]+@[A-za-z]+\.[A-za-z]{2,}$')
        attr_n = re.compile(r'^[a-z]+$')
        pattern1 = re.compile(r'^[A-za-z]+$')
        if ids != "":
            args = ids.split()
            class_name = self.checkGlobalClass(args[0])
            if (args and len(args) == 1):
                idMatch = re.match(p, args[0])
                clMatch = re.match(pattern1, args[0])
                if idMatch:
                    print("** class name is missing **")
                elif (clMatch and args[0] == "BaseModel"):
                    print("** instance id missing **")
            elif (args and len(args) >= 2):
                klas, id, attr_name, attr_value = args
                if (attr_name or attr_value == ""):
                    attr_name = ""
                    attr_value = ""
                """update method called"""
                if class_name == args[0]:
                    self.call_update(id, attr_name, attr_value)
            elif (args and len(args) > 3):
                print("Invalid input. Usage: update <attr_name> <attr_value>")
        else:
            print("** class name is missing **")

    def call_update(self, id, attr_name, attr_value):
        """ method powers the update functionality
            and is called from do_update method
        """
        if os.path.exists("file.json"):
            with open("file.json", "r") as f:
                json_str = json.load(f)
                updId = ""
                for key, value in json_str.items():
                    entryId = value.get('id')
                    entryClass = value.get('__class__')
                    if entryId == id:
                        updId = f"{entryClass}.{entryId}"
                if updId in json_str:
                    if (attr_name == ""):
                        print("** attribute name missing **")
                elif (attr_value == ""):
                    print("** value missing **")
                else:
                    print("** no instance found **")
        else:
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

    """def modify_json(self, value):
        strs = []
        obj1 = value
        function call to convert "time" to suit requirement
        time_c = self.time_convert(obj1)
        model_name = f"[{obj['__class__']}]"
        model_id = "(" + value["id"] + ")"
        model_attr = str(value)
        model_instance = f"{model_name} {model_id} {model_attr}"
        strs.append(model_instance)
        result = "[" + ", ".join(strs) + "]"
        return result"""

    """def call_do_all(self, file, cmarg):
        method to execute do_all
        if cmarg == "":
            pass
        if cmarg != "":
            args = cmarg.split()
            if (args[0] != "BaseModel"):
                    print("** class name doesn't exist **")
        a=""
        for key, value in file.items():
            if cmarg != "":
                id_value = value.get('__class__')
                if id_value == args[0]:
                    a = self.modify_json(value)
            else:
                a = self.modify_json(value)
            return a;
     """
