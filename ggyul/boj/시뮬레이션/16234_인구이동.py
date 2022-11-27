from collections import deque

N, L, R = map(int, input().split())
popl = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 1
while True:
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            # 열린 곳 모두 탐색
            queue = deque()
            countries = []
            queue.append((i, j))  # 탐색용 큐
            countries.append((i, j))  # 탐색한 나라 저장
            all_sum = popl[i][j]  # 전체 합 구함
            while queue:
                r, c = queue.pop()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                for dir in range(4):
                    nr = r + dx[dir]
                    nc = c + dy[dir]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if L <= abs(popl[r][c] - popl[nr][nc]) <= R:
                            queue.append((nr, nc))
                            countries.append((nr, nc))
                            all_sum += popl[nr][nc]
            if len(countries) <= 1:  # 연결된 나라 없음
                continue
            count += len(countries)
            for r, c in countries:
                popl[r][c] = all_sum//len(countries)
    if count <= 0:
        ans -= 1
        break
    ans += 1
print(ans)