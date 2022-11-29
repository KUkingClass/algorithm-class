'''
https://www.acmicpc.net/problem/3584
가장 가까운 공통 조상
가장 가까운 공통 조상: 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드를
**자기 자신도 자손이다** (예제 2번)
t * n, n = 10,000이므로 매번 한 depth씩 확인해도 시간초과가 나지 않는다.
'''
import sys
sys.setrecursionlimit(10005) # N = 10,000

def dfs(node, depth, depths):
    depths[node] = depth
    for next in tree[node]:
        dfs(next, depth + 1, depths)


t = int(input())
for _ in range(t):
    n = int(input())
    parents = [0] * (n + 1)
    depths = [0] * (n + 1)
    tree = [[] for _ in range(n+1)]
    for i in range(n - 1):
        # a가 b의 부모
        a, b = map(int, input().split())
        tree[a].append(b)
        parents[b] = a
    x, y = map(int, input().split())
    # 부모 찾기
    root = parents.index(0, 1, len(parents))
    dfs(root, 0, depths)
    while x != y:
        if depths[x] == depths[y]:
            # 높이가 같으므로 둘다 올린다
            x = parents[x]
            y = parents[y]
        else:
            if depths[x] > depths[y]:
                x = parents[x]
            else:
                y = parents[y]
    print(x)
