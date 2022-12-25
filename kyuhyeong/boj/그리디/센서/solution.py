import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    positions = sorted(list(map(int, sys.stdin.readline().split())))

    distance = []
    for i, position in enumerate(positions[:-1]):
        distance.append(positions[i + 1] - position)

    print(sum(sorted(distance)[:n - k]))
