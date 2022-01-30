#!/usr/bin/python3
"""
Python console file
"""
import cmd
import sys
from models.engine.file_storage import FileStorage

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
            print("*** name require")
            return
        elif args not in FileStorage.classes():
            print("no class")
            return
        base = FileStorage.classes()[args]()
        base.name = args
        base.save()
        return
    
    def do_all(self, args):
        """access BaseModel \n"""
        data = FileStorage()
        if args:
            if args not in FileStorage.classes():
                print("** class doesn't exist **")
                return
            for k, v in data.all().items():
                if (type(v).__name__) == args:
                    data = {k: v.to_dict()}
            print (data)
            return
        for k, v in data.all().items():
            data = v
            print(data)
        return

    def findModel(fun):
        """ remove item from json file"""
        def wrapper(self, args):
            data = FileStorage().all()
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
                return
            elif args[0] not in FileStorage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            try:
                fun(self, data[str(".".join(args))])
            except KeyError:
                print("** no instance found **")
                return
        return wrapper


    @findModel
    def do_show(self, args):
        """ print class instance """
        print(args)
        return
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
