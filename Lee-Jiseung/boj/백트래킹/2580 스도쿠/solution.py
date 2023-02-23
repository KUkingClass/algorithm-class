import sys


def backtracking(r, c):
    global board, flag
    if flag:
        return
    if c == 9:
        c = 0
        r += 1
    if r == 9:
        flag = True
        for line in board:
            print(*line, sep=' ')
        return

    if board[r][c] != 0:
        backtracking(r, c+1)
        return

    for i in range(1, 10):
        if not column(r, i):
            continue
        if not row(c, i):
            continue
        if not box(r, c, i):
            continue
        board[r][c] = i
        backtracking(r, c+1)
        board[r][c] = 0


def column(r, i):
    global board
    for j in range(9):
        if board[r][j] == i:
            return False
    return True


def row(c, i):
    global board
    for j in range(9):
        if board[j][c] == i:
            return False
    return True


def box(r, c, i):
    global board
    for j in range(3):
        for k in range(3):
            if board[r // 3 * 3 + j][c // 3 * 3 + k] == i:
                return False
    return True


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
flag = False
backtracking(0, 0)
