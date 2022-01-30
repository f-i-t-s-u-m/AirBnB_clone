#!/usr/bin/python3
"""
Python console file
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ class if HBHB command """
    prompt = '(hbtn) '

    def do_quite(self, arg):
        """Quit command to exit the program \n"""
        return True

    def do_EOF(self, argfs):
        """Quit command to exit the program \n"""
        return True

    def emptyline(self):
        """ show nothing \n"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
