# 18258 큐 2
# https://www.acmicpc.net/problem/18258
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for _ in range(N):
    word = list(map(str, input().split()))
    if word[0] == 'push':
        queue.append(word[1])
    elif word[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif word[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)