# https://www.acmicpc.net/problem/2164
# 카드 2
# N=500_000이므로 N번 시뮬레이션 해보면 된다
from collections import deque
n = int(input())
deq = deque([i+1 for i in range(n)])
while len(deq) > 1:
    deq.popleft()
    left = deq.popleft()
    deq.append(left)
print(deq[0])
