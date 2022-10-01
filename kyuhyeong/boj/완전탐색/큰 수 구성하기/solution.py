import sys
from itertools import product

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    set_k = list(map(int, sys.stdin.readline().split()))

    answer = 0
    for repeat in range(1, len(str(n)) + 1):
        for s in product(set_k, repeat=repeat):
            i = int("".join(map(str, s)))
            if i <= n:
                answer = max(answer, i)

    print(answer)
