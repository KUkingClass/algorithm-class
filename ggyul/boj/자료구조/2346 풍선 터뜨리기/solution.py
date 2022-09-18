# https://www.acmicpc.net/problem/2346
# 풍선 터뜨리기
from collections import deque
n = int(input())
ans = []
values = list(map(int, input().split()))
deq = deque(tuple([i+1, values[i]]) for i in range(len(values)))
while len(deq)>1:
    index, offset = deq.popleft()
    ans.append(index)        
    if offset > 0:
        while offset > 1:
            tup = deq.popleft()
            deq.append(tup)
            offset-=1
    else:
        offset = -offset
        while offset > 0:
            tup = deq.pop()
            deq.appendleft(tup)
            offset -= 1
index, offset = deq.popleft()
ans.append(index)
print(' '.join(map(str, ans)))
