import sys
from collections import deque


def make_tree(tree_size):
    tree = {}
    for _ in range(tree_size - 1):
        parent, child = map(int, sys.stdin.readline().split())
        if parent not in tree:
            tree[parent] = {"parent": -1, "children": [child], "depth": 0}
        else:
            tree[parent]["children"].append(child)
        if child not in tree:
            tree[child] = {"parent": parent, "children": [], "depth": 0}
        else:
            tree[child]["parent"] = parent

    return tree


def find_root(tree):
    for node, info in tree.items():
        if info["parent"] == -1:
            return node


def set_depth(tree, root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        queue.extend(tree[node]["children"])
        for child in tree[node]["children"]:
            tree[child]["depth"] = tree[node]["depth"] + 1


def find_lca(tree, node1, node2):
    while tree[node1]["depth"] > tree[node2]["depth"]:
        node1 = tree[node1]["parent"]
    while tree[node2]["depth"] > tree[node1]["depth"]:
        node2 = tree[node2]["parent"]

    while node1 != node2:
        node1 = tree[node1]["parent"]
        node2 = tree[node2]["parent"]

    return node1


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        tree_size = int(sys.stdin.readline())
        tree = make_tree(tree_size)

        root = find_root(tree)
        set_depth(tree, root)

        node1, node2 = map(int, sys.stdin.readline().split())
        print(find_lca(tree, node1, node2))
