import sys


def backtracking(hand):
    global n, eggs, answer
    if hand == n:
        count = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                count += 1
        answer = max(answer, count)
        return
    if eggs[hand][0] <= 0:
        backtracking(hand+1)
        return
    flag = True
    for i in range(n):
        if i == hand:
            continue
        if eggs[i][0] <= 0:
            continue
        flag = False
        eggs[hand][0] -= eggs[i][1]
        eggs[i][0] -= eggs[hand][1]
        backtracking(hand+1)
        eggs[hand][0] += eggs[i][1]
        eggs[i][0] += eggs[hand][1]
    if flag:
        backtracking(hand+1)


n = int(sys.stdin.readline())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
backtracking(0)
print(answer)
