#!/usr/bin/python3
"""Base Model Class Test"""

from cmd import Cmd


class HBNBCommand(Cmd):
    """HBNB Command Shell"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Handles empty lines by doing nothing\n"""

    def do_EOF(self, line) -> bool | None:
        """Handles EOF (Ctrl+D) to exit the shell\n"""
        return True

    def do_quit(self, line) -> bool | None:
        """Quit command to exit the program\n"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """List available commands with 'help'
        If given a command name, provide specific help"""
        return super().do_help(arg)

    def do_hbnb(self, line) -> bool | None:
        """Handle hbnb as a general handler for hbnb.* commands\n"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
