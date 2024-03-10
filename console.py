#!/usr/bin/env python3

""" Command Interpreter """
import cmd
import os
import json
import re
from datetime import datetime
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
                elif (clMatch and args[0] != "BaseModel"):
                    print("** class doesn't exist **")
                elif (clMatch and args[0] == "BaseModel"):
                    print("** instance id missing **")
            elif (args and len(args) == 2):
                klas, id = args
                if os.path.exists("file.json"):
                    with open("file.json", "r") as f:
                        json_str = json.load(f)
                        """print(json_str)"""
                        for key, value in json_str.items():
                            id_value = value.get('id')
                            """print(id)"""
                            if id_value == id:
                                obj = BaseModel(**value)
                                print(f"{obj}")
                        if id != id_value:
                            print("** no instance found **")
                else:
                    pass
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
        if os.path.exists("file.json"):
            with open("file.json", "r") as f:
                json_str = json.load(f)
            strs = []
            if (line != ""):
                args = line.split()
                if (args[0] != "BaseModel"):
                    print("** class name doesn't exist **")
                else:
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

    def do_destroy(self, ids):
        """ Deletes an obj/instance based on its id"""
        p = re.compile(r'^[\da-fA-F]{8}(-[\da-fA-F]{4}){3}-[\da-fA-F]{12}$')
        pattern1 = re.compile(r'^[A-za-z]+$')
        if ids != "":
            args = ids.split()
            if (args and len(args) == 1):
                idMatch = re.match(p, args[0])
                clMatch = re.match(pattern1, args[0])
                if idMatch:
                    print("** class name is missing **")
                elif (clMatch and args[0] != "BaseModel"):
                    print("** class doesn't exist **")
                elif (clMatch and args[0] == "BaseModel"):
                    print("** instance id missing **")
            elif (args and len(args) == 2):
                klas, id = args
                if os.path.exists("file.json"):
                    with open("file.json", "r") as f:
                        json_str = json.load(f)
                        if id in json_str:
                            del json_str[id]
                        if id not in json_str:
                            print("** no instance found **")
                    """with open("file.json", 'w') as file:
                        json.dump(json_str, file, indent=4)"""
                else:
                    pass
            elif (args and len(args) > 2):
                print("Invalid input. Usage: show  <class> <id>")
        else:
            print("** class name is missing **")

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
