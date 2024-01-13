#!/usr/bin/python3
"""Base Model Class Test"""

import cmd
from re import compile, search
from operations import create, all, count, destroy, show, update, update_obj, check, check_cls, cmd_options
# from operations import *


class HBNBCommand(cmd.Cmd):
    """HBNB Command Shell"""

    prompt = "(hbnb) "

    __all_re = compile(r"(.*?).all\( *\)$")
    __count_re = compile(r"([\w-]*?).count\( *\)$")
    __show_re = compile(r"([\w-]*?).show\( *([\w-]*?) *\)$")
    __destroy_re = compile(r"([\w-]*?).destroy\( *([\w-]*?) *\)$")
    __update_re = compile(
        r"([\w-]*?).update\( *([\w-]*?) *, *([\w-]*?) *, *([\"\'\w-]*?) *\)$")
    __update_obj_re = compile(
        r"([\w-]*?).update\( *([\w-]*?) *, *({.*?}) *\)$")

    def emptyline(self) -> None:
        """Handles empty lines by doing nothing\n"""

    def do_EOF(self, line: str) -> bool:
        """Handles EOF (Ctrl+D) to exit the shell\n"""
        return True

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line: str) -> None:
        """Create command"""
        create(*cmd_options(line, 1))

    def do_show(self, line: str) -> None:
        """Show command"""
        show(*cmd_options(line, 2))

    def do_destroy(self, line: str) -> None:
        """Destroy command"""
        destroy(*cmd_options(line, 2))

    def do_all(self, line: str) -> None:
        """List all instances of a class"""
        all(*cmd_options(line, 1))

    def do_update(self, line: str) -> None:
        """Update an attribute value for an object."""
        update(*cmd_options(line, 4))

    def default(self, line: str) -> None:
        """Default handler when no specific handler is found"""
        if (search(self.__all_re, line)):
            all(*self.__all_re.findall(line))
        elif (search(self.__count_re, line)):
            count(*self.__count_re.findall(line))
        elif (search(self.__show_re, line)):
            show(*self.__show_re.findall(line)[0])
        elif (search(self.__destroy_re, line)):
            destroy(*self.__destroy_re.findall(line)[0])
        elif (search(self.__update_re, line)):
            update(*self.__update_re.findall(line)[0])
        elif (search(self.__update_obj_re, line)):
            update_obj(*self.__update_obj_re.findall(line)[0])
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
