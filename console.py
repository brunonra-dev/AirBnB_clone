"""
Console - entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


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

        lsplit = line.split()
        if len(l) == 1:
            lsplit.append("")

        for cls in self.cls_list:
            if cls == lsplit[0]:
                all_objs = storage.all()
                for k in all_objs.keys():
                    if all_objs[k].id == l[1]:
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
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
