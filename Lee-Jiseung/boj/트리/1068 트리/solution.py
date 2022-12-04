import sys
from collections import deque

n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
node = int(sys.stdin.readline())
activated = [True] * n

dq = deque()
dq.append(node)
while dq:
    cur = dq.popleft()
    activated[cur] = False
    for i, parent in enumerate(parents):
        if parent == cur:
            dq.append(i)
            
answer = 0
for i, parent in enumerate(parents):
    if not activated[i]:
        continue
    flag = 1
    for j, p in enumerate(parents):
        if p == i and activated[j]:
            flag = 0
            break
    answer += flag
print(answer)