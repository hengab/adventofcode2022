import os
import typing as typ
import sys


class TreeNode(object):
    def __init__(self, node_name, parent_tree_node):
        self.name: str = node_name
        self.parent: typ.Optional[TreeNode] = parent_tree_node
        self.branches: typ.List[TreeNode] = []
        self.files: typ.List[typ.Tuple[str, int]] = []

    def size(self) -> int:
        size = sum([file[1] for file in self.files])

        return size + sum([branch.size() for branch in self.branches])

    def __str__(self):
        size = self.size()
        return f"{self.name} {self.files} - Total: {size}"

    def relevant_size(self) -> int:
        size = self.size()
        branche_sizes = sum([branch.relevant_size() for branch in self.branches])
        if size > 100000:
            size = 0

        return size + branche_sizes
    
    def smallest_dir(self, needed_space):
        size = self.size()
        min_branch_size = min([branch.smallest_dir(needed_space) for branch in self.branches] + [sys.maxsize])
        if size < min_branch_size and size >= needed_space:
            min_branch_size = size
        
        return min_branch_size


def print_tree(tree: TreeNode, base_name: str = ""):
    print(f"{base_name}/{tree}")
    for branch in tree.branches:
        print_tree(branch, f"{base_name}/{tree.name}")


root_node: TreeNode = TreeNode("/", None)
current_node: TreeNode = root_node
# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for line in input_file.readlines():
        print(current_node)
        line = line.strip()
        if line.startswith("$ cd /"):
            current_node = root_node
        elif line.startswith("$ cd .."):
            current_node = current_node.parent
        elif line.startswith("$ cd"):
            new_branch = TreeNode(line[5:], current_node)
            current_node.branches.append(new_branch)
            current_node = new_branch
        elif line.startswith("$ ls"):
            ...
        elif line.startswith("dir"):
            ...
        else:
            parts = line.split(" ")
            current_node.files.append((parts[1], int(parts[0])))


print("-------------------")
print_tree(root_node)
print(f"Part 1 Size: {root_node.relevant_size()}")
needed_space = 30000000 - (70000000 - root_node.size())
# print(f"Needed Space: {needed_space}")
smallest = root_node.smallest_dir(needed_space)
print(f"Part 2 Size:: {smallest}")
