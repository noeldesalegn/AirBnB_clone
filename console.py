#!/usr/bin/python3
"""Console.py"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """pass"""
        pass

    def do_EOF(self, line):
        """EOF to quit"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
