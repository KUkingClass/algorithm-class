import sys
from collections import deque


def solution(R, C, T):
    room = []
    cleaner = []
    for i in range(R):
        row = list(map(int, sys.stdin.readline().split()))
        if -1 in row:
            cleaner.append(i)
        room.append(row)

    for _ in range(T):
        room = diffuse(room, R, C)
        clean(room, cleaner, R, C)

    return sum(map(sum, room)) + 2


def diffuse(room, R, C):
    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]
    room_copy = [[i for i in row] for row in room]

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1:
                diffuse_amount = room[i][j] // 5
                if diffuse_amount == 0:
                    continue
                diffuse_count = 0
                for di, dj, in zip(dis, djs):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        diffuse_count += 1
                        room_copy[ni][nj] += diffuse_amount
                room_copy[i][j] -= diffuse_amount * diffuse_count

    return room_copy


def clean(room, cleaner, R, C):
    cleaner1 = cleaner[0]
    cleaner2 = cleaner[1]

    queue1 = deque()
    queue2 = deque()

    for j in range(1, C):
        queue1.append(room[cleaner1][j])
    for i in range(cleaner1 - 1, -1, -1):
        queue1.append(room[i][C - 1])
    for j in range(C - 2, -1, -1):
        queue1.append(room[0][j])
    for i in range(1, cleaner1):
        queue1.append(room[i][0])

    for j in range(1, C):
        queue2.append(room[cleaner2][j])
    for i in range(cleaner2 + 1, R):
        queue2.append(room[i][C - 1])
    for j in range(C - 2, -1, -1):
        queue2.append(room[R - 1][j])
    for i in range(R - 2, cleaner2, -1):
        queue2.append(room[i][0])

    queue1.rotate(1)
    queue1[0] = 0
    queue2.rotate(1)
    queue2[0] = 0

    for j in range(1, C):
        room[cleaner1][j] = queue1.popleft()
    for i in range(cleaner1 - 1, -1, -1):
        room[i][C - 1] = queue1.popleft()
    for j in range(C - 2, -1, -1):
        room[0][j] = queue1.popleft()
    for i in range(1, cleaner1):
        room[i][0] = queue1.popleft()

    for j in range(1, C):
        room[cleaner2][j] = queue2.popleft()
    for i in range(cleaner2 + 1, R):
        room[i][C - 1] = queue2.popleft()
    for j in range(C - 2, -1, -1):
        room[R - 1][j] = queue2.popleft()
    for i in range(R - 2, cleaner2, -1):
        room[i][0] = queue2.popleft()


if __name__ == '__main__':
    R, C, T = map(int, sys.stdin.readline().split())
    print(solution(R, C, T))
