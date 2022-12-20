"""
https://www.acmicpc.net/problem/1715
카드 정렬하기

식을 써보면
카드가 a, b, c, d, e...있을 때
(a+b) + ((a+b)+c) + (((a+b)+c))+d + ...
따라서 가장 작은 숫 두개를 계속해서 뽑는 게 최소값이다.
"""
import sys
import heapq

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))
count = 0
while len(cards) >= 2:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    count += a+b
    heapq.heappush(cards, a+b)
print(count)
