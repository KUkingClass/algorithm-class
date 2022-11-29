'''
https://www.acmicpc.net/problem/11437
LCA
17M
MN = 50,000 * 10,000 = 500,000,000 = 5억이므로 아슬하지만
매번 depth 1씩 확인해도 통과한다.
(PyPy말고 Python으로는 시간초과)
'''
import sys

sys.setrecursionlimit(50_005)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
# 부모 - 자식은 아니고 그냥 연결된 관계
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
depths = [-1] * (n + 1)
parents = [-1] * (n + 1)


def dfs(node, parent, depth):
    if depths[node] >= 0:
        return
    depths[node] = depth
    parents[node] = parent
    for next in graph[node]:
        dfs(next, node, depth + 1)


# 루트는 1번
dfs(1, 0, 0)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    while x != y:
        if depths[x] > depths[y]:
            x = parents[x]
        elif depths[x] < depths[y]:
            y = parents[y]
        else:
            x = parents[x]
            y = parents[y]
    print(x)
