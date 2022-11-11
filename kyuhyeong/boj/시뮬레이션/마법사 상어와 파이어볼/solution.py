import sys

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    fireballs = []
    labels = [[[] for _ in range(N)] for _ in range(N)]
    directions = {
        0: (-1, 0),
        1: (-1, 1),
        2: (0, 1),
        3: (1, 1),
        4: (1, 0),
        5: (1, -1),
        6: (0, -1),
        7: (-1, -1)
    }
    even_directions = [0, 2, 4, 6]
    odd_directions = [1, 3, 5, 7]

    for _ in range(M):
        fireballs.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(K):
        while fireballs:
            r, c, m, s, d = fireballs.pop()
            r -= 1
            c -= 1
            next_direction = directions[d]

            r = (r + s * next_direction[0]) % N
            c = (c + s * next_direction[1]) % N
            if d % 2 != 0 and not (0 <= r < N and 0 <= c < N):
                r += next_direction[0]
                c += next_direction[1]

            labels[r][c].append([r, c, m, s, d])

        for i in range(N):
            for j in range(N):
                if labels[i][j]:
                    if len(labels[i][j]) == 1:
                        fireballs.append(labels[i][j].pop())
                        continue
                    mass_total = 0
                    speed_total = 0
                    odd = even = 0

                    while labels[i][j]:
                        r, c, m, s, d = labels[i][j].pop()
                        mass_total += m
                        speed_total += s
                        if d % 2 == 0:
                            even += 1
                        else:
                            odd += 1

                    mass = mass_total // 5
                    if mass == 0:
                        continue
                    speed = speed_total // (odd + even)
                    if odd == 0 or even == 0:
                        for d in even_directions:
                            fireballs.append([i, j, mass, speed, d])
                    else:
                        for d in odd_directions:
                            fireballs.append([i, j, mass, speed, d])

    print(sum(list(zip(*fireballs))[2]) if fireballs else 0)
