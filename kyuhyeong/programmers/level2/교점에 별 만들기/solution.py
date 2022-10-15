from math import inf


def solution(line):
    answer = []
    min_x, min_y = inf, inf
    max_x, max_y = -inf, -inf

    for i in range(len(line) - 1):
        a1, b1, c1 = line[i]
        for j in range(i + 1, len(line)):
            a2, b2, c2 = line[j]

            if a2*b1 == a1*b2:
                continue

            x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
            y = (a1 * c2 - a2 * c1) / (a2 * b1 - a1 * b2)

            if float.is_integer(x) and float.is_integer(y):
                x = int(x)
                y = int(y)
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                answer.append((x, y))

    plane = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for x, y in answer:
        i = max_y - y
        j = x - min_x
        plane[i][j] = "*"

    return list(map("".join, plane))


if __name__ == '__main__':
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    # line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
    # line = [[1, -1, 0], [2, -1, 0]]
    print(solution(line))
