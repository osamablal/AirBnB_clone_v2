#!/usr/bin/python3
"""Defines the HBNB console.

This module provides a command-line interface (CLI) for interacting with the
HolbertonBnB project. It includes commands for creating, updating, and managing
instances of various classes, such as BaseModel, User, State, City, Amenity,
Place, and Review.

"""

import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    This class inherits from the cmd.Cmd module to create an interactive
    command-line interpreter. It includes commands for managing instances
    of various classes.

    Attributes:
        prompt (str): The command prompt displayed to the user.
        __classes (set): A set of valid class names for object creation.

    Methods:
        emptyline(): Ignores empty input.
        do_quit(line): Exits the program.
        do_EOF(line): Exits the program upon receiving the EOF signal.
        do_create(line): Creates a new instance of a specified class.
        do_show(line): Displays the string representation of an instance.
        do_destroy(line): Deletes an instance based on class name and id.
        do_all(line): Displays string representations of instances.
        do_update(line): Updates an instance by adding or updating attributes.
        count(line): Counts the number of instances of a class.
        strip_clean(args): Strips the argument and returns a cleaned string.
        default(line): Handles default behavior for unknown commands.

    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignores empty input."""
        pass

    def do_quit(self, line):
        """Exits the program.

        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.

        """
        return True

    def do_EOF(self, line):
        """Exits the program upon receiving the EOF signal.

        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.

        """
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of a specified class.

        Args:
            line (str): The command line input.

        Raises:
            SyntaxError: If class name is missing.
            NameError: If the specified class does not exist.

        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Displays the string representation of an instance.

        Args:
            line (str): The command line input.

        Raises:
            SyntaxError: If class name is missing.
            NameError: If the specified class does not exist.
            IndexError: If instance id is missing.
            KeyError: If no valid instance is found.

        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id.

        Args:
            line (str): The command line input.

        Raises:
            SyntaxError: If class name is missing.
            NameError: If the specified class does not exist.
            IndexError: If instance id is missing.
            KeyError: If no valid instance is found.

        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if
