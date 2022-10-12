import sys
sys.setrecursionlimit(10**9)


def tree_search(tree, remain, node=1, count=0):
    cur_node = tree[node]

    if cur_node["children"][0] != -1 and not tree[cur_node["children"][0]]["visit"]:
        return tree_search(tree, remain, cur_node["children"][0], count + 1)

    if not cur_node["visit"]:
        cur_node["visit"] = True
        remain -= 1
        if not remain:
            return count

    if cur_node["children"][1] != -1 and not tree[cur_node["children"][1]]["visit"]:
        return tree_search(tree, remain, cur_node["children"][1], count + 1)
    if cur_node["parent"] != -1:
        return tree_search(tree, remain, cur_node["parent"], count + 1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    tree = {i: {"parent": -1, "children": [], "visit": False} for i in range(1, n + 1)}

    for _ in range(n):
        node, a, b = map(int, sys.stdin.readline().split())
        tree[node]["children"].extend([a, b])
        if a != -1:
            tree[a]["parent"] = node
        if b != -1:
            tree[b]["parent"] = node

    print(tree_search(tree, n))
