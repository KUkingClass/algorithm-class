import sys
import heapq

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cards = []
    for _ in range(n):
        cards.append(int(sys.stdin.readline()))

    heapq.heapify(cards)

    answer = 0
    for _ in range(n - 1):
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        answer += card1 + card2
        heapq.heappush(cards, card1 + card2)

    print(answer)
