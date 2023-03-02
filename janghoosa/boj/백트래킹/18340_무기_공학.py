# 18340 무기 공학
# https://www.acmicpc.net/problem/18430

def solve(x, y, sum):
    global res
    if y == M:
        y = 0
        x += 1
    if x == N:
        res = max(res, sum)
        return
    for shape in boomerang:
        x1, y1 = x+shape[0][0], y+shape[0][1]
        x2, y2 = x+shape[1][0], y+shape[1][1]
        x3, y3 = x+shape[2][0], y+shape[2][1]
        x4, y4 = x+shape[3][0], y+shape[3][1]
        if 0 <= x1 < N and 0 <= y1 < M and 0 <= x2 < N and 0 <= y2 < M and 0 <= x3 < N and 0 <= y3 < M:
            if not visited[x1][y1] and not visited[x2][y2] and not visited[x3][y3]:
                weight = wood[x1][y1] + wood[x2][y2] + \
                    wood[x3][y3] + wood[x4][y4]
                visited[x1][y1] = visited[x2][y2] = visited[x3][y3] = True
                solve(x, y+1, sum+weight)
                visited[x1][y1] = visited[x2][y2] = visited[x3][y3] = False
    solve(x,y+1,sum)

N, M = map(int, input().split())
wood = [list(map(int, input().split())) for _ in range(N)]
# 앞 3개는 모양, 마지막 1개는 중복
boomerang = [
    [(0, 0), (0, 1), (1, 1), (0, 1)],
    [(1, 0), (0, 1), (1, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 0)],
    [(0, 0), (1, 0), (0, 1), (0, 0)]
]
res = 0
visited = list([False]*M for _ in range(N))
solve(0, 0, 0)
print(res)
