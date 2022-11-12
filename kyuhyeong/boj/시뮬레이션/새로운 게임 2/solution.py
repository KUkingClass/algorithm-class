import sys


def solution(N, K):
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, sys.stdin.readline().split())))

    game_status = [[[] for _ in range(N)] for _ in range(N)]
    piece_positions = {}
    directions = {
        1: (0, 1),
        2: (0, -1),
        3: (-1, 0),
        4: (1, 0)
    }

    for i in range(K):
        r, c, d = map(int, sys.stdin.readline().split())
        r -= 1
        c -= 1
        game_status[r][c].append([i, directions[d]])
        piece_positions[i] = [r, c]

    for turn in range(1, 1001):
        for piece in range(K):
            r, c = piece_positions[piece]
            start_idx = 0
            for idx, elem in enumerate(game_status[r][c]):
                element_num, _ = elem
                if element_num == piece:
                    start_idx = idx
                    break
            group = game_status[r][c][start_idx:]
            for _ in range(len(game_status[r][c]) - start_idx):
                game_status[r][c].pop()

            if move(game_map, game_status, piece_positions, group, [r, c]):
                return turn

    return -1


def move(game_map, game_status, piece_positions, group, cur_position):
    r, c = cur_position
    r, c, next_direction = get_next_position_direction(game_map, r, c, group[0][1])
    next_pos_info = get_position_info(game_map, r, c)

    group[0][1] = next_direction

    if next_pos_info == "white":
        game_status[r][c].extend(group)
    elif next_pos_info == "red":
        game_status[r][c].extend(group[::-1])
    else:
        r, c = cur_position
        game_status[r][c].extend(group)

    for g in group:
        piece_positions[g[0]] = [r, c]
    if len(game_status[r][c]) >= 4:
        return True

    return False


def get_next_position_direction(board, r, c, direction):
    next_r = r + direction[0]
    next_c = c + direction[1]

    if next_r < 0 or next_c < 0 or next_r >= len(board) or next_c >= len(board) or board[next_r][next_c] == 2:
        next_direction = [-direction[0], -direction[1]]
        return r + next_direction[0], c + next_direction[1], next_direction

    return next_r, next_c, direction


def get_position_info(board, r, c):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board) or board[r][c] == 2:
        return "blue"
    elif board[r][c] == 1:
        return "red"
    return "white"


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    print(solution(N, K))
