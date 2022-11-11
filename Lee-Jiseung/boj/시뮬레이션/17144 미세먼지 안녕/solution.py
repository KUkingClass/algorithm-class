import sys

r, c, t = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
airfilter = 0
upcycle = []
downcycle = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(r):
    if grid[i][0] == -1:
        airfilter = i
        grid[airfilter][0] = 0
        grid[airfilter + 1][0] = 0
        break

for i in range(airfilter - 1, -1, -1):
    upcycle.append([i, 0])
for i in range(1, c):
    upcycle.append([0, i])
for i in range(1, airfilter):
    upcycle.append([i, c - 1])
for i in range(c - 1, -1, -1):
    upcycle.append([airfilter, i])

for i in range(airfilter + 2, r):
    downcycle.append([i, 0])
for i in range(1, c):
    downcycle.append([r - 1, i])
for i in range(r - 1, airfilter, -1):
    downcycle.append([i, c - 1])
for i in range(c - 1, -1, -1):
    downcycle.append([airfilter + 1, i])

for _ in range(t):
    new_grid = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] <= 0:
                continue

            count = 0
            for dri, dci in zip(dr, dc):
                newi = i + dri
                newj = j + dci

                if newi < 0 or newi >= r or newj < 0 or newj >= c or ((newi == airfilter or newi == airfilter + 1) and newj == 0):
                    continue

                new_grid[newi][newj] += grid[i][j] // 5
                count += 1
            new_grid[i][j] += grid[i][j] - grid[i][j] // 5 * count
    grid = new_grid

    for i in range(1, len(upcycle)):
        grid[upcycle[i - 1][0]][upcycle[i - 1][1]] = grid[upcycle[i][0]][upcycle[i][1]]
    for i in range(1, len(downcycle)):
        grid[downcycle[i - 1][0]][downcycle[i - 1][1]] = grid[downcycle[i][0]][downcycle[i][1]]

print(sum([sum(row) for row in grid]))