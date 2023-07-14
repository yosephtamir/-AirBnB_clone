#!/usr/bin/python3
"""
This module acts as a command interpreter
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
