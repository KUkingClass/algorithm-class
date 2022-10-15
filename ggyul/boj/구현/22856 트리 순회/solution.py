'''
https://www.acmicpc.net/problem/22856
트리 순회
'''

import sys
sys.setrecursionlimit(100_005)
_input = sys.stdin.readline


class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


n = int(input())

tree = [Node() for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, _input().split())
    if b != -1:
        tree[a].left = b
        tree[b].parent = a
    if c != -1:
        tree[a].right = c
        tree[c].parent = a

#1. 유사 중위 순회 끝 찾기
visited = [False]*(n+1)
end_of_seach = -1


def in_order(node):
    left = tree[node].left
    right = tree[node].right
    if left != -1:
        in_order(left)
    global end_of_seach
    end_of_seach = node
    if right != -1:
        in_order(right)


in_order(1)

#2. 유사 중위 순회
ans = -1  # 맨 처음 루트 방문은 제외
visited = [False]*(n+1)
node = 1
while True:
    ans += 1
    if not visited[node]:
        visited[node] = True
    parent = tree[node].parent
    left = tree[node].left
    right = tree[node].right
    if left != -1 and not visited[left]:
        node = left
    elif right != -1 and not visited[right]:
        node = right
    elif node == end_of_seach:
        break
    elif parent != -1:
        node = parent

print(ans)
