#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
import models
from models.user import User

class HBNBCommand(cmd.Cmd):
    """defines the HBNBCommand interpreter"""
    prompt = "(hbnb) "

    __classes = {"BaseModel", "user"}

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
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            class_name = arg.split()[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            try:
                instances = eval(class_name).all()
                print([str(instance) for instance in instances])
            except AttributeError:
                print("** class doesn't have attribute all **")
                return

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
