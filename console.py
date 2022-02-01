#!/usr/bin/python3
"""
Python console file
"""
import cmd
import re
import json
from models import storage 


class HBNBCommand(cmd.Cmd):
    """ class if HBHB command """
    prompt = '(hbtn) '

    def default(self, line):
        """ redirect to _precmd if command not found"""
        self._precmd(line)

    def _precmd(self, line):
        """run if no command found"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

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
        """ update an instance \n"""
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


    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
