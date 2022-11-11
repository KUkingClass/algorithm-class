import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= grid[i][j] <= 5:
            cctv.append([i, j])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cctv_types = [[[0], [1], [2], [3]],
              [[0, 2], [1, 3]],
              [[0, 1], [1, 2], [2, 3], [3, 0]],
              [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
              [[0, 1, 2, 3]]]

candidates = [grid]

for i, j in cctv:
    new_candidates = []

    for cctv_type in cctv_types[grid[i][j] - 1]:
        for candidate in candidates:
            new_candidate = copy.deepcopy(candidate)
            for d in cctv_type:
                newi = i + dr[d]
                newj = j + dc[d]
                while 0 <= newi < n and 0 <= newj < m and new_candidate[newi][newj] != 6:
                    if new_candidate[newi][newj] == 0:
                        new_candidate[newi][newj] = -1

                    newi += dr[d]
                    newj += dc[d]
                    
            new_candidates.append(new_candidate)

    candidates = new_candidates


answer = n * m
for candidate in candidates:
    answer = min(answer, sum(map(lambda x: x.count(0), candidate)))
print(answer)
