import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    dna = [sys.stdin.readline().strip() for _ in range(n)]

    answer = ""
    hamming_distance = 0
    for i in range(m):
        nucleo = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for j in range(n):
            nucleo[dna[j][i]] += 1
        max_key = sorted([k for k, v in nucleo.items() if max(nucleo.values()) == v])[0]
        answer += max_key
        hamming_distance += n - nucleo[max_key]

    print(answer)
    print(hamming_distance)
