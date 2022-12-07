"""
https://school.programmers.co.kr/learn/courses/30/lessons/81302#
거리두기 확인하기

한 방향으로 두번 가는 경우를 생각 못해서 한시간 걸렸다
"""

SIZE = 5
HUMAN = 'P'
TABLE = 'O'
PARTITION = 'X'
next_dirs = [
    # 우, 하우, 우우
    [(0, 1), (1, 1), (0, 2)],
    # 하, 하우, 하좌, 하하
    [(1, 0), (1, 1), (1, -1), (2, 0)],
    # 좌, 하좌
    [(0, -1), (1, -1)],
]


def is_with_distance(place, x, y):
    if place[x][y] != HUMAN:
        return True
    for dirs in next_dirs:
        is_blocked = True
        for i, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                continue
            target = place[nx][ny]
            if i == 0:
                is_blocked = (target == PARTITION)
            if not is_blocked and target == HUMAN:
                return False
    return True


def check_distance(place):
    for i in range(SIZE):
        for j in range(SIZE):
            if not is_with_distance(place, i, j):
                return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))
    return answer


if __name__ == '__main__':
    res = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
    print(res)
