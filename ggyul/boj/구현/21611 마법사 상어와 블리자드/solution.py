'''
https://www.acmicpc.net/problem/21611
마법사 상어와 블리자드
'''
# 입력
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
magics = []
for _ in range(m):
    magics.append(list(map(int, input().split())))
    magics[-1][0] -= 1


def is_in_range(coor):
    return 0 <= coor[0] < n and 0 <= coor[1] < n


magic_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
marble_dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우, 상, 좌, 하
board_num = [[0] * n for _ in range(n)]
# 다음 구슬 방향 채워놓기
board_num[n // 2][n // 2 - 1] = 1

marble_lines = [0, board[n // 2][n // 2 - 1]]


def fill_num():
    num = 2
    dir = 0
    coor = [n // 2 + 1, n // 2 - 1]
    loop_cnt = 2
    while True:
        for _ in range(2):
            for _ in range(loop_cnt):
                board_num[coor[0]][coor[1]] = num
                # 1차원으로 기억
                marble_lines.append(board[coor[0]][coor[1]])
                num += 1
                coor[0] += marble_dir[dir][0]
                coor[1] += marble_dir[dir][1]
                if not is_in_range(coor):
                    return
            dir = (dir + 1) % len(marble_dir)
        loop_cnt += 1


fill_num()


def move(marble_lines):
    new_lines = [0] * len(marble_lines)
    point = 1
    new_point = 1
    while 0 < point < len(marble_lines) and 0 < new_point < len(marble_lines):
        color = marble_lines[point]
        point += 1
        if color == 0:
            continue
        new_lines[new_point] = color
        new_point += 1
    return new_lines


ans = [0, 0, 0]  # 폭발한 구슬 개수

for magic in magics:
    # 1. 블리자드
    d, s = magic
    coor = [n // 2, n // 2]
    count = 0
    while is_in_range(coor) and count <= s:
        index = board_num[coor[0]][coor[1]]
        # if marble_lines[index] != 0:
        #     ans[marble_lines[index] - 1] += 1
        marble_lines[index] = 0
        coor[0] += magic_dir[d][0]
        coor[1] += magic_dir[d][1]
        count += 1
    marble_lines = move(marble_lines)
    # 2. 폭발하기
    while True:
        is_explode = False
        point = 1
        while 0 < point < len(marble_lines):
            color = marble_lines[point]
            if color == 0:
                point += 1
                continue
            count = 1
            next = point + 1
            while next < len(marble_lines):
                next_color = marble_lines[next]
                if color == next_color:
                    count += 1
                elif next_color != 0:
                    break
                next += 1
            if count >= 4:
                is_explode = True
                for i in range(point, next):
                    if marble_lines[i] == 0:
                        continue
                    ans[color - 1] += 1
                    marble_lines[i] = 0
            point = next
        marble_lines = move(marble_lines)
        if is_explode:
            point = 1
        else:
            break
    # 변화하기
    new_lines = [0] * len(marble_lines)
    point = 1
    new_point = 1
    while 0 < point < len(marble_lines) and 0 < new_point < len(marble_lines):
        color = marble_lines[point]
        if color == 0:
            point += 1
            continue
        count = 1
        next = point + 1
        while next < len(marble_lines):
            next_color = marble_lines[next]
            if color == next_color:
                count += 1
            elif next_color != 0:
                break
            next += 1
        new_lines[new_point] = count
        new_point += 1
        if new_point < len(marble_lines):
            new_lines[new_point] = color
            new_point += 1
        point = next
    marble_lines = new_lines
print(1 * ans[0] + 2 * ans[1] + 3 * ans[2])
