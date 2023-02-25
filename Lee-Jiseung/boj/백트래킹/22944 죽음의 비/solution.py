import sys


def backtracking(r, c, flag, hp, umbrella_hp, count):
    global n, d, umbrellas, end, answer
    if count >= answer:
        return
    dist = abs(r - end[0]) + abs(c - end[1])
    if dist < hp + umbrella_hp:
        answer = min(answer, count+dist)
    for i in range(len(umbrellas)):
        if flag & (1<<i):
            continue
        dist = abs(r - umbrellas[i][0]) + abs(c - umbrellas[i][1])
        if dist >= hp + umbrella_hp:
            continue
        backtracking(umbrellas[i][0], umbrellas[i][1], flag | (1<<i), min(hp, hp+umbrella_hp-dist), d, count+dist)


n, h, d = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
umbrellas = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start = [i, j]
        elif board[i][j] == 'E':
            end = [i, j]
        elif board[i][j] == 'U':
            umbrellas.append([i, j])
answer = 500**3
backtracking(start[0], start[1], 0, h, 1, 0)
print(answer if answer!=500**3 else -1)
