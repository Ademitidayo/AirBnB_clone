#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """defines the HBNBCommand interpreter"""
    prompt = "(hbnb) "

    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def parse(arg):
        """Define regular expression patterns"""
        class_name_pattern = r"([A-Za-z_]\w*)"
        method_call_pattern = r"\.all\(\)"

        full_pattern = f"{class_name_pattern}{method_call_pattern}"
        match = re.match(full_pattern, arg)
        if match:
            class_name = match.group(1)
            return class_name
        else:
            curly_braces = re.search(r"\{(.*?)\}", arg)
            brackets = re.search(r"\[(.*?)\]", arg)
            if curly_braces is None:
                if brackets is None:
                    return [i.strip(",") for i in arg.split()]
                else:
                    lexer = arg.split(arg[:brackets.span()[0]])
                    retl = [i.strip(",") for i in lexer]
                    retl.append(brackets.group())
                    return retl
            else:
                lexer = arg.split(arg[:curly_braces.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(curly_braces.group())
                return retl

    
    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True
    def do_quit(self,arg):
        """Quit command to exit the program"""
        return True
    def do_show(self,arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        obj = models.storage.get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        obj = storage.get(key)
        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not args:
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                objl = []
                for obj in storage.all().values():
                    if len(args) > 0 and args[0] == obj.__class__.__name__:
                        objl.append(obj.__str__())
                    elif len(args) == 0:
                        objl.append(obj.__str__())
                print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        obj = models.storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        print("Retrieved object:", obj)
        print("Updating attribute:", attr_name, "with value:", attr_value)
        setattr(obj, attr_name, attr_value)
        models.storage.save()
        print("Changes saved successfully.")

    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = arg.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
if __name__ == '__main__':
    HBNBCommand().cmdloop()
