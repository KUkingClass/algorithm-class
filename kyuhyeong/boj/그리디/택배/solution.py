import sys

if __name__ == '__main__':
    n, capacity = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    requests = []
    for _ in range(m):
        sender, receiver, boxes = map(int, sys.stdin.readline().split())
        requests.append((receiver, boxes, sender))

    requests.sort()
    answer = 0
    towns = [capacity for _ in range(n + 1)]

    for dst, weight, src in requests:
        carry_weight = min(min(towns[src: dst]), weight)
        answer += carry_weight
        for i in range(src, dst):
            towns[i] -= carry_weight

    print(answer)
