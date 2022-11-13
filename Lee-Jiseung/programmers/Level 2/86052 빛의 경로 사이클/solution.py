def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            for d in range(4):
                newr = r
                newc = c
                l = 0
                init_d = d

                while True:
                    if newr == r and newc == c and l > 0 and d == init_d:
                        answer.append(l)
                        break
                    if visited[r][c][d]:
                        break
                    visited[r][c][d] = True

                    r = (r + dr[d] + n) % n
                    c = (c + dc[d] + m) % m
                    if grid[r][c] == 'L':
                        d = (d + 3) % 4
                    elif grid[r][c] == 'R':
                        d = (d + 1) % 4
                    l += 1

    answer = sorted(answer)
    return answer