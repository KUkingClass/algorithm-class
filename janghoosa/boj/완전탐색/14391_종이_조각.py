# 14391 종이 조각
# https://www.acmicpc.net/problem/14391
N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
ans = 0
for i in range(1 << N * M):
    total = 0
    for row in range(N):
        srow = 0
        for col in range(M):
            idx = row * M + col
            if i & (1 << idx) != 0:
                srow = srow * 10 + A[row][col]
            else:
                total += srow
                srow = 0
        total += srow

    for col in range(M):
        scol = 0
        for row in range(N):
            idx = row * M + col
            if i & (1 << idx) == 0:
                scol = scol * 10 + A[row][col]
            else:
                total += scol
                scol = 0
        total += scol
    ans = max(ans, total)
print(ans)