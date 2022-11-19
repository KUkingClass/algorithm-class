import sys
from itertools import product
from math import inf


def solution(n, m):
    room = []
    cameras = {}
    cam_idx = 0
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if 1 <= row[j] <= 5:
                cameras[cam_idx] = [row[j], [i, j]]
                cam_idx += 1
        room.append(row)

    min_blind_spot = inf

    rotate_permutations = product(range(4), repeat=cam_idx)
    for permutation in rotate_permutations:
        room_copy = [[i for i in row] for row in room]
        for cam_num, rotate_num in enumerate(permutation):
            cam_type, position = cameras[cam_num]
            scan(room_copy, cam_type, position, rotate_num)
        min_blind_spot = min(min_blind_spot, sum(row.count(0) for row in room_copy))

    return min_blind_spot


def scan(room, cam_type, position, direction):
    if cam_type == 1:
        scan_range = cam1(direction)
    elif cam_type == 2:
        scan_range = cam2(direction)
    elif cam_type == 3:
        scan_range = cam3(direction)
    elif cam_type == 4:
        scan_range = cam4(direction)
    else:
        scan_range = cam5(direction)

    for di, dj in scan_range:
        i, j = position
        while True:
            i += di
            j += dj
            if 0 <= i < len(room) and 0 <= j < len(room[0]):
                if room[i][j] == 0:
                    room[i][j] = "#"
                elif room[i][j] == 6:
                    break
            else:
                break


def cam1(direction):
    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]

    return [list(zip(dis, djs))[direction]]


def cam2(direction):
    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]

    if direction % 2 == 0:
        return [[dis[0], djs[0]], [dis[2], djs[2]]]
    else:
        return [[dis[1], djs[1]], [dis[3], djs[3]]]


def cam3(direction):
    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]

    return [[dis[direction % 4], djs[direction % 4]], [dis[(direction + 1) % 4], djs[(direction + 1) % 4]]]


def cam4(direction):
    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]
    search_direction = list(zip(dis, djs))
    scan_range = []

    for i in range(4):
        if i != direction:
            scan_range.append([*search_direction[i]])

    return scan_range


def cam5(direction):
    return [[0, 1], [1, 0], [0, -1], [-1, 0]]


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    print(solution(n, m))
