# https://www.acmicpc.net/problem/18258
# 큐 2
import sys
from collections import deque
n = int(input())
que = deque()
for i in range(n):
    opers = sys.stdin.readline().split()
    if opers[0]=='push':
        que.append(int(opers[1]))
    elif opers[0] == 'pop':
        print(que.popleft()) if que else print(-1)
    elif opers[0] == 'size':
        print(len(que))
    elif opers[0] == 'empty':
        print(0) if que else print(1)
    elif opers[0] == 'front':
        print(que[0]) if que else print(-1)
    elif opers[0] == 'back':
        print(que[-1]) if que else print(-1)
