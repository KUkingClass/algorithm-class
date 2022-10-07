# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# https://www.acmicpc.net/problem/2422
from itertools import combinations
N, M = map(int, input().split())
A = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
combi = list(combinations(range(1, N+1), 3))
ans = 0
for i1, i2, i3 in combi:
    if i1 not in A[i2] and i1 not in A[i3] and i2 not in A[i3]:
        ans += 1
print(ans)
