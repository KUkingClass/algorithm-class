import sys
import heapq

n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]
cards = sorted(cards)

answer = 0
while len(cards) != 1:
    count = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, count)
    answer += count
print(answer)