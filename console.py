#!/usr/bin/python3
"""
This module acts as a command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the command interpreter class
    """

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """
        Used to exit out of the console
        """
        return True

    def emptyline(self):
        """
        Empty line should not do anything
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """
        create the BaseModel instance
        """
        if len(arg) == 0:
            print("** class name missing ** ")
            return
        else:
            token = arg.split()
            try:
                instance = eval(token[0])()
                instance.save()
                print(instance.id)
            except:
                print("** class name missing ** ")
    
    def do_show(self, arg):
        """
        print the string representation of the class
        based on the class name and id of the instance
        """
        
        token = arg.split()
        if len(token) == 0:
                print("** class name missing **")
                return
        elif len(token) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                eval(token[0])
            except:
                print("** class doesn't exist **")
    
            try:
                inst_dict = storage.all()
                inst_id = token[0] + "." + token[1]
                values = inst_dict[inst_id]
                print(values)
            except:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """
        print the string representation of the class
        based on the class name and id of the instance
        """
        
        token = arg.split()
        if len(token) == 0:
            print("** class name missing **")
            return
        elif len(token) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                eval(token[0])
            except:
                print("** class doesn't exist **")
    
            try:
                inst_dict = storage.all()
                inst_id = token[0] + "." + token[1]
                del inst_dict[inst_id]
                storage.save()
            except:
                print("** no instance found **")
    
    def do_all(self, arg):
        """
        print the string representation of the classed passed as the arg
        """
        my_classes = {"BaseModel":BaseModel}
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif len(arg) != 0:
            token = arg.split()
            if token[0] not in my_classes:
                print("**class doesn't exist **")
                return
            dictionaries = storage.all()
            print([str(val) for key, val in dictionaries.items() if arg in key])
        else:
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
