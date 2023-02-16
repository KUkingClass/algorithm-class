import sys


def backtracking(r, c, power):
    global n, m, nums, used, answer
    if c == m:
        c = 0
        r += 1
    if r == n:
        answer = max(answer, power)
        return

    backtracking(r, c+1, power)
    if used[r][c]:
        return

    for i in range(4):
        newr = r + dr[(i+1)%4 if i%2 == 0 else i]
        newc = c + dc[i if i%2 == 0 else (i+1)%4]
        if 0 <= newc < m and 0 <= newr < n:
            if not used[r][newc] and not used[newr][c]:
                used[r][c] = True
                used[r][newc] = True
                used[newr][c] = True
                backtracking(r, c+1, power + nums[r][c]*2 + nums[r][newc] + nums[newr][c])
                used[r][c] = False
                used[r][newc] = False
                used[newr][c] = False


n, m = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
used = [[False for _ in range(m)] for _ in range(n)]
answer = 0
dr = [0, 1, 0, -1] # 좌하우상
dc = [-1, 0, 1, 0]
backtracking(0, 0, 0)
print(answer)
