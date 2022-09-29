import sys
from collections import Counter

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    dnas = list(zip(*[sys.stdin.readline().strip() for _ in range(n)]))
    answer = ""
    distance = 0
    for dna in dnas:
        nucleotide, count = sorted(Counter(dna).most_common(), key=lambda pair: (-pair[1], pair[0]))[0]
        answer += nucleotide
        distance += n - count

    print(answer)
    print(distance)
