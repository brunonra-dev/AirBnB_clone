"""
Console - entry point of the command interpreter
"""
import cmd
from posixpath import split
from shlex import shlex
from models import storage
import models
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    cls_list = ["BaseModel"]

    @staticmethod
    def check_classes(lsplit):
        """check classes"""
        for k in storage.classes.keys():
            if k == lsplit[0]:
                return 1

        return 0

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        return True

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        print(f"{obj.id}")

    def do_show(self, line):
        if line == "":
            print("** class name missing **")
            return

        l_split = line.split()
        if len(l_split) == 1:
            l_split.append("")

        for cls in self.cls_list:
            if cls == l_split[0]:
                all_objs = storage.all()
                for k in all_objs.keys():
                    if all_objs[k].id == l_split[1]:
                        print(all_objs[k])
                        return
                print("** instance id missing **")
                return

        print("** class doesn't exist **")

    def do_destroy(self, line):
        if line == "":
            print("** class name missing **")
            return

        lsplit = line.split()
        if len(lsplit) == 1:
            print("** instance id missing **")
            return

        if self.check_classes(lsplit[0]):
            for k in storage.__objects.keys():
                if storage.__objects[k].id == lsplit[1]:
                    del storage.__objects[k]
                    return
            print("** no instance found **")
            return

        print("** class doesn't exist **")

    def do_all(self, line):
        split_line = line.split()
        count = 1
        if line != "":
            for cls in self.cls_list:
                if cls != split_line[0]:
                    count = 0
                else:
                    count = 1
        if count == 0:
            print("** class doesn't exist **")
            return
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
            return

    def do_update(self, line):
        split_line = shlex.split(line)
        count = 1
        if len(split_line) == 0:
            print("** class name missing **")
            return
        for cls in self.cls_list:
            if cls != split_line[0]:
                count = 0
            else:
                count = 1
        if count == 0:
            print("** class doesn't exist **")
            return
        if len(split_line) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        correct_id = ""
        for k in all_objs.keys():
            if all_objs[k].id == split_line[1]:
                correct_id = split_line[1]
        if correct_id == "":
            print("** no instance found **")
            return
        if len(split_line) == 2:
            print("** attribute name missing **")
            return
        if len(split_line) == 3:
            print("** value missing **")
        setattr(models.storage.all()[k], split_line[2], split_line[3])
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
