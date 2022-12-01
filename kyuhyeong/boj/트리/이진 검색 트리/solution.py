import sys
sys.setrecursionlimit(20000)

"""
1. 일단 파이썬에서는 시간초과가 난다.
range(10000)으로 수동으로 입력했을때 대략 15초정도 걸리는듯
pypy로 제출하면 통과한다.

2. 재귀 깊이 설정에서 평소처럼 10**9로 설정했더니 메모리 초과가 떴다.
recursionlimit 만으로 메모리 차이가 난다는게 신기하긴 한데 1만~2만으로 줄이니까 통과했다.
실행 시 메모리가 무려 240mb 가까이 쓰여서 아슬아슬하게 통과했다.
"""
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def add_node(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    add_node(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    add_node(node.right, value)

        if self.root is None:
            self.root = Node(value)
        else:
            add_node(self.root, value)

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    tree = BinaryTree()

    while True:
        val = sys.stdin.readline().strip()
        if val != "":
            tree.insert(int(val))
        else:
            break

    tree.postorder(tree.root)
