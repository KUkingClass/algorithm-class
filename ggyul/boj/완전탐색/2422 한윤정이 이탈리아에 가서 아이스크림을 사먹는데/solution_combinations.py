'''
https://www.acmicpc.net/problem/2422
한윤정이 이탈리아에 가서 아이스크림을 사먹는데
'''
from itertools import combinations
n, m = map(int, input().split())
is_bad = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    ice1, ice2 = map(int, input().split())
    is_bad[ice1][ice2] = True
    is_bad[ice2][ice1] = True
combis = list(combinations([i for i in range(1, n+1)], 3))
ans = 0
for combi in combis:
    if is_bad[combi[0]][combi[1]] or is_bad[combi[0]][combi[2]] or is_bad[combi[1]][combi[2]]:
        continue
    ans += 1
print(ans)
