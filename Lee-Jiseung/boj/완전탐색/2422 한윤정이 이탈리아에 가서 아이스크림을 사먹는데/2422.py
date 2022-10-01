import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
inputs = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    inputs[x][y] = 1
    inputs[y][x] = 1

if n < 3:
    print(0)
else:
    answer = 0
    choose3 = list(combinations([i+1 for i in range(n)], 3))
    for choose in choose3:
        if inputs[choose[0]][choose[1]] + inputs[choose[1]][choose[2]] + inputs[choose[2]][choose[0]] == 0:
            answer += 1
    print(answer)