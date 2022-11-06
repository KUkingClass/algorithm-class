import sys
from collections import deque

if __name__ == '__main__':
    N, L, R = map(int, sys.stdin.readline().split())
    countries = []

    for _ in range(N):
        countries.append(list(map(int, sys.stdin.readline().split())))

    dis = [-1, 0, 1, 0]
    djs = [0, 1, 0, -1]

    queue = deque()
    answer = 0

    for iteration in range(1, 2001):
        visit = [[False for _ in range(N)] for _ in range(N)]

        group_num = 0
        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    visit[i][j] = True
                    queue.append([i, j])
                    group = []
                    group_sum = 0

                    while queue:
                        cur_i, cur_j = queue.popleft()
                        group.append([cur_i, cur_j])
                        group_sum += countries[cur_i][cur_j]

                        for di, dj in zip(dis, djs):
                            next_i = cur_i + di
                            next_j = cur_j + dj
                            if 0 <= next_i < N and 0 <= next_j < N and not visit[next_i][next_j] and \
                                    L <= abs(countries[cur_i][cur_j] - countries[next_i][next_j]) <= R:
                                queue.append([next_i, next_j])
                                visit[next_i][next_j] = True

                    for group_i, group_j in group:
                        countries[group_i][group_j] = group_sum // len(group)

                    group_num += 1

        if group_num == N**2:
            answer = iteration - 1
            break

    print(answer)
