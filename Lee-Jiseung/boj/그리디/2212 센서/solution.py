import sys


def solution():
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    sensors = list(set(list(map(int, sys.stdin.readline().split()))))
    sensors = sorted(sensors)
    if len(sensors) <= k:
        print(0)
        return

    distances = [(i, sensors[i+1]-sensors[i]) for i in range(len(sensors)-1)]
    distances = sorted(sorted(distances, key=lambda x: -x[1])[:k-1], key=lambda x: x[0])

    answer = 0
    left = 0
    for i in range(k-1):
        answer += sensors[distances[i][0]] - sensors[left]
        left = distances[i][0]+1
    print(answer + sensors[-1] - sensors[left])


solution()
