# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
from queue import Queue
import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())

queue = Queue()
for i in range(1, n+1):
    queue.put(i)

ans = []
while queue.qsize() > 0:
    for i in range(k-1):
        top = queue.get()
        queue.put(top)
    ans.append(queue.get())

print('{}{}{}'.format('<', ', '.join(map(str, ans)), '>'))
