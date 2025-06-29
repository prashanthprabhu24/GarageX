import os

"""
This python file contains my self written implementation of using recursion to traverse nested folder and create file structure as tree.
This is not part of book. Rather my Experiment.
"""


def print_tree(path, indent=""):
    if not os.path.exists(path):
        print(f"{indent}❌ Path does not exist: {path}")
        return
    print(indent + os.path.basename(path) + "/")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print_tree(full_path, indent + "│   ")
        else:
            print(indent + "├── " + item)


root = "MainFolder"
print_tree(root)
