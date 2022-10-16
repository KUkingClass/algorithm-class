from itertools import combinations
import itertools

r, c = map(int, input().split())
lamps = [[0]*c for _ in range(r)]
for i in range(r):
    lamps[i] = list(map(int, input()))
k = int(input())

ans = 0
pressed = [False]*c
cols = [i for i in range(c)]
combs = itertools.combinations(cols, k)
for comb in combs:
    for num in comb:
        pressed[num] = True
    print(pressed)
    row_count = 0
    for i in range(r):
        is_on = True
        for j in range(c):
            if not((lamps[i][j] == 0) ^ pressed[j]):     
                is_on=False
                break
        if is_on:
            row_count+=1
    ans = max(ans, row_count)
print(ans)