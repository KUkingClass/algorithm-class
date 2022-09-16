import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cards = deque(range(1, n + 1))
    length = len(cards)

    while len(cards) > 1:
        cards.popleft()
        cards.rotate(-1)

    print(cards[0])
