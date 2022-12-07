"""
https://www.acmicpc.net/problem/1068
트리
11M

노드의 최대 개수가 50밖에 안되므로
트리를 만들 때 해당 노드를 parent에 연결하지 않는다.
그럼 트리를 전체 탐색할 때 해당 노드는 탐색하지 않는다.
"""

from collections import defaultdict, deque

n = int(input())
parent_infos = list(map(int, input().split()))
target = int(input())

# defaultdict는 dict에 해당 key의 value가 없을 때 기본으로 만들어준다
tree = defaultdict(list)
root = -1
for i, parent in enumerate(parent_infos):
    if parent == -1:
        root = i
    elif i != target:
        tree[parent].append(i)
if root == target:
    print(0)
else:
    q = deque()
    q.append(root)
    ans = 0
    while q:
        node = q.popleft()
        if node not in tree:
            ans += 1
        else:
            for children in tree[node]:
                q.append(children)
    print(ans)
