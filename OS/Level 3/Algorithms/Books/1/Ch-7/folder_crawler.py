import os
from collections import deque

"""
This python file contains my self written implementation of tree traversal for print file names in nested folder based on books explanation and code.
Here the search is exactly BFS, if you think of folders and files as Nodes in Graph.
"""

def print_file_names(folder):
    queue = deque()
    queue.append(folder)
    while queue:
        sub_folder = queue.popleft()
        for file in os.listdir(sub_folder):
            path = sub_folder+"/"+file
            if os.path.isfile(path):
                print(file)
            else:
                queue.append(path)

root_folder = "MainFolder"
print_file_names(root_folder)
