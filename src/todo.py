import os
from pathlib import Path


class Prompt:
    def __init__(self):
        pass

    def welcome(self):
        print(f"Welcome to todopy!\n")
        print(f"1. List todo lists")
        print(f"2. Read todo lists")
        print(f"3. Append to todo lists")
        print(f"4. Remove Lines from todo lists")
        print(f"5. Delete todo lists")
        print(f"6. Create todo lists")
        print(f"7. Exit")
        self.number_of_options = 7
        try:
            self.main_input = int(input(f"\nSelect an option:\n"))
            print("")
        except ValueError:
            print("Input must be an integer!")
        if self.main_input not in [i for i in range(1, self.number_of_options + 1)]:
            raise Exception(f"Input must range from 1 to {self.number_of_options}")
        return self.number_of_options

    def process_input(self):
        while True:
            match self.main_input:
                # list todo lists
                case 1:
                    print("Following todo lists exist:\n")
                    todo.read_dir()
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # read todo lists
                case 2:
                    todo.get_file_path()
                    todo.recursively_print_lists()
                    print("")
                    sub_input = int(input("Which file do you wish to read?:\n"))
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.read_file(todo_file)
                    print(f"{todo.file_content}")
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # append to a todo file
                case 3:
                    todo.get_file_path()
                    todo.recursively_print_lists()
                    print("")
                    sub_input = int(input("Which file do you wish to append to?:\n"))
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.append_file(todo_file)
                    todo.read_file(todo_file)
                    print(f"{todo.file_content}")
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # remove a todo list entry (line)
                case 4:
                    todo.get_file_path()
                    todo.recursively_print_lists()
                    print("")
                    sub_input = int(
                        input(
                            "Which todo list do you wish to remove a todo entry from?:\n"
                        )
                    )
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.remove_todo_entry(todo_file)
                    todo.print_line_by_line(todo_file)
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # remove a todo list
                case 5:
                    todo.get_file_path()
                    todo.recursively_print_lists()
                    print("")
                    sub_input = int(input("Which todo list do you wish to delete?:\n"))
                    print("")
                    todo_file = todo.list_of_filepaths[sub_input - 1]
                    todo.delete_todo_list(todo_file)
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # create a todo lsit
                case 6:
                    todo.get_file_path()
                    todo.recursively_print_lists()
                    print("")
                    filename = input("What should be the filename?:\n")
                    print("")
                    filename = filename.strip().lower()
                    todo.create_file(filename)
                    self.check_if_done()
                    if self.check_value == True:
                        break
                    elif self.check_value == False:
                        pass
                    self.welcome()
                # leave the program
                case 7:
                    print("See you next time!")
                    break

    def check_if_done(self):
        check_if_done = input("Was that all? (y/n):\n")
        print("")
        check_if_done = check_if_done.lower().strip()
        if check_if_done == "y":
            self.check_value = True
        elif check_if_done == "n":
            self.check_value = False
        else:
            raise Exception("Input must be either y or n!")
        return self.check_value

    def initial_check(self):
        if os.path.exists(todo.dirname):
            pass
        else:
            os.mkdir(todo.dirname)

        for e in os.scandir(todo.dirname):
            if e.is_file():
                with open(e.path, "r") as f:
                    todo.file_list.append(e.path)

        if todo.file_list == []:
            creation_user_input = input(
                "\nIt seems you haven't yet created a todo list, would you wish to do so? (y/n):\n"
            )
            creation_user_input = creation_user_input.lower().strip()
            print("")
            if creation_user_input == "y":
                filename = input("What should be the filename?:\n")
                print("")
                filename = filename.strip().lower()
                todo.create_file(filename)
            elif creation_user_input == "n":
                pass
            else:
                raise Exception("You must either enter y or n!")
        else:
            pass


class Todo:
    def __init__(self):
        self.dirname = f"{Path.home()}/.config/todopy/"
        self.file_list = list()
        pass

    def create_file(self, filename: str):
        with open(f"{self.dirname}/{filename}.txt", "w") as f:
            header = input(
                "What should be the header of the newly created todo list?:\n"
            )
            f.write(f"{header}\n")
            print("")

    def read_file(self, todo_file: str):
        self.file_content_list = list()
        with open(todo_file, "r") as f:
            self.file_content = f.read()
        return self.file_content

    def print_line_by_line(self, todo_file: str):
        n = 1
        with open(f"{todo_file}", "r") as f:
            for entry in f:
                print(f"{n}. {entry}".rstrip())
                n += 1
        print("")

    def get_file_path(self):
        self.list_of_filepaths = list()
        self.names_of_filepaths = list()
        for e in os.scandir(self.dirname):
            if e.is_file():
                self.list_of_filepaths.append(e.path)
                self.names_of_filepaths.append(e.name)
        return self.list_of_filepaths, self.names_of_filepaths

    def read_dir(self):
        for e in os.scandir(self.dirname):
            if e.is_file():
                with open(e.path, "r") as f:
                    print(f"{e.name}:")
                    print(f"{f.readline().rstrip('\n')}")
                    print("")

    def delete_todo_list(self, todo_file: str):
        os.remove(f"{todo_file}")

    def append_file(self, todo_file: str):
        self.read_file(todo_file)
        print(self.file_content)
        with open(todo_file, "a") as f:
            f.write(
                f"- "
                + input(f"What do you wish to append to your TO-DO entry?:\n")
                + "\n"
            )
        print("")

    def remove_todo_entry(self, todo_file: str):
        self.print_line_by_line(todo_file)
        self.file_input = int(input("Which line do you wish to remove?:\n"))
        print("")
        if self.file_input == 1:
            user_input = input(
                "You cannot remove the header!\nDo you wish to change it instead? (y/n):\n"
            )
            print("")
            user_input = user_input.strip().lower()
            if user_input == "y":
                with open(todo_file, "r") as fr:
                    lines = fr.readlines()
                new_header = (
                    input("What do you wish for the new header to be?:\n") + "\n"
                )
                print("")
                if len(lines) > 0:
                    lines[0] = new_header
                else:
                    lines.append(new_header)
                with open(todo_file, "w") as f:
                    f.writelines(lines)
            elif user_input == "n":
                pass
            else:
                raise Exception("Input must be either y or n!")
        else:
            with open(todo_file, "r") as fr:
                self.lines = fr.readlines()
                n = 1
            with open(todo_file, "w") as f:
                for line in self.lines:
                    if n != self.file_input:
                        f.write(line)
                    n += 1

    def recursively_print_lists(self):
        n = 1
        for i in todo.names_of_filepaths:
            print(f"{n}. {i}")
            n += 1


todo = Todo()
welcome = Prompt()

if __name__ == "__main__":
    welcome.initial_check()
    welcome.welcome()
    welcome.process_input()
