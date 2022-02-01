#!/usr/bin/python3
"""
Python console file
"""
import cmd
import sys
import re
from models import storage 

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
    
    def do_create(self, args):
        """ Creates a new instance \n"""
        if args == "":
            print("** class name missing **")
            return
        elif args not in storage.classes():
            print("** class doesn't exist **")
            return
        base = storage.classes()[args]()
        base.name = args
        base.save()
        print(base.__dict__['id'])
        return
    
    def do_all(self, args):
        """access BaseModel \n"""
        if args:
            if args not in storage.classes():
                print("** class doesn't exist **")
                return
            data = [str(v) for k, v in storage.all().items()
                if type(v).__name__ == args]
            print (data)
            return
        data = [str(v) for k, v in storage.all().items()]
        print(data)
        return

    def findModel(fun):
        """ method to act as decorator 
            for show and destory
        """
        def wrapper(self, args):
            """ inner function to do validation"""
            data = storage.all()
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
                return
            elif args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            try:
                fun(self, args)
            except KeyError:
                print("** no instance found **")
                return
        return wrapper


    @findModel
    def do_show(self, args):
        """ print class instance \n"""
        print(storage.all()[".".join(args[:2])])
        return

    @findModel
    def do_destory(self, args):
        """ deletes an instance based on the class name and id \n"""
        del storage.all()[".".join(args[:2])]
        return
    
    @findModel
    def do_update(self, args):
        """ update an instance"""
        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        val = args[3].replace('"', '')
        if(val.isdigit()):
            val = int(val)
        elif(re.search('^[+-]?[0-9]+\.[0-9]+$', val)):
            val = float(val)
        data = storage.all()[".".join(args[:2])].__dict__
        data[args[2]] = val
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
