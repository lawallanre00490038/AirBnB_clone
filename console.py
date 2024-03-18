#!/usr/bin/python3
""" Module for HBNB command interpreter. """

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
  """ HBNB console class """

  prompt = "(hbnb) "

  def emptyline(self):
    """ Empty line method"""
    pass

  def do_create(self, arg):
    """ Create new instance """
    if not arg:
      print("** class name missing **")
      return
    elif arg[0] == "User":
      new_instance = User()
      new_instance.save()
      print(new_instance.id)
    arg = arg.split()
    try:
      new_instance = eval(arg[0])()
      new_instance.save()
      print(new_instance.id)
    except NameError:
      print("** class doesn't exist **")


  def do_show(self, arg):
    """ Show instance method """
    if not arg:
      print("** class name missing **")
      return
    elif arg[0] == "User":
      if len(arg) < 2:
        print("** instance id missing **")
        return
      key = "{}.{}".format(arg[0], arg[1])
      if key in storage.all():
        print(storage.all()[key])
      else:
        print("** no instance found **")
    arg = arg.split()
    try:
      if len(arg) < 2:
        raise ValueError
      all_objs = storage.all()
      key = arg[0] + '.' + arg[1]
      print(all_objs[key])
    except KeyError:
      print("** no instance found **")
    except ValueError:
      print("** instance id missing **")
    except NameError:
      print("** class doesn't exist **")

  def do_destroy(self, arg):
    """ Destroy instance method """
    if not arg:
      print("** class name missing **")
      return
    elif arg[0] == "User":
      if len(arg) < 2:
        print("** instance id missing **")
        return
      key = "{}.{}".format(arg[0], arg[1])
      if key in storage.all():
        del storage.all()[key]
        storage.save()
      else:
        print("** no instance found **")
      return
    arg = arg.split()
    try:
      if len(arg) < 2:
          raise ValueError
      all_objs = storage.all()
      key = arg[0] + '.' + arg[1]
      del all_objs[key]
      storage.save()
    except KeyError:
      print("** no instance found **")
    except ValueError:
      print("** instance id missing **")
    except NameError:
      print("** class doesn't exist **")

  def do_all(self, arg):
    """ Print all instances method """
    all_objs = storage.all()
    if arg:
      try:
        all_objs = {k: v for k, v in all_objs.items() if type(v).__name__ == arg}
      except NameError:
        print("** class doesn't exist **")
        return
    elif arg[0] == "User":
      objs = storage.all()
      obj_list = []
      for key, value in objs.items():
        if arg[0] in key:
          obj_list.append(str(value))
      print(obj_list)
    print([str(v) for v in all_objs.values()])

  def do_update(self, arg):
    """ Update instance method """
    if not arg:
        print("** class name missing **")
        return
    elif arg[0] == "User":
      if len(arg) < 2:
        print("** instance id missing **")
        return
      key = "{}.{}".format(arg[0], arg[1])
      if key not in storage.all():
        print("** no instance found **")
        return
      if len(arg) < 3:
        print("** attribute name missing **")
        return
      if len(arg) < 4:
        print("** value missing **")
        return
      setattr(storage.all()[key], arg[2], arg[3])
      storage.all()[key].save()
    arg = shlex.split(arg)
    try:
      if len(arg) < 2:
        raise ValueError
      all_objs = storage.all()
      key = arg[0] + '.' + arg[1]
      obj = all_objs[key]
      if len(arg) < 3:
        raise ValueError
      if len(arg) < 4:
        raise NameError
      if len(arg) > 4:
        raise SyntaxError
      setattr(obj, arg[2], eval(arg[3]))
      storage.save()
    except KeyError:
      print("** no instance found **")
    except ValueError:
      print("** instance id missing **")
    except NameError:
      print("** attribute name missing **")
    except SyntaxError:
      print("** value missing **")
    except AttributeError:
      print("** no instance found **")

  def do_quit(self, arg):
    """ Quit method """
    return True

  def do_EOF(self, arg):
    """ EOF method """
    return True

if __name__ == "__main__":
  HBNBCommand().cmdloop()
