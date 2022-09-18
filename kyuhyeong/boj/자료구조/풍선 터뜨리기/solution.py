import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    papers = list(map(int, sys.stdin.readline().split()))

    balloons = deque(range(1, n + 1))
    answer = []

    while balloons:
        cur_pop = balloons.popleft()
        answer.append(cur_pop)
        next_pop = papers[cur_pop - 1]
        if next_pop > 0:
            balloons.rotate(-next_pop + 1)
        else:
            balloons.rotate(-next_pop)

    print(" ".join(map(str, answer)))
