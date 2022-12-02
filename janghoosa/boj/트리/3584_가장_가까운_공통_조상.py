# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상
T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0]*(N+1)
    for _ in range(N-1):
        i, j = map(int, input().split())
        parent[j] = i

    a, b = map(int, input().split())
    a_parent = [a]
    b_parent = [b]

    while parent[a]:
        a_parent.append(parent[a])
        a=parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b=parent[b]

    a_parent.reverse()
    b_parent.reverse()

    a_depth = len(a_parent)-1
    b_depth = len(b_parent)-1

    index = min(a_depth, b_depth)
    
    while a_parent[index] != b_parent[index]:
        index -= 1

    print(a_parent[index])