import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    towers = list(map(int, sys.stdin.readline().split()))

    answer = ["0" for _ in range(n)]
    prev_height = towers[-1]
    unassigned = []

    for i in range(n - 2, -1, -1):
        cur_height = towers[i]
        if cur_height > prev_height:
            answer[i + 1] = str(i + 1)
            while unassigned:
                if unassigned[-1][1] > cur_height:
                    break
                answer[unassigned[-1][0]] = str(i + 1)
                unassigned.pop()
        else:
            unassigned.append((i + 1, prev_height))

        prev_height = cur_height

    print(" ".join(answer))
