INF = 1 << 64-1


def solution(lines):
    answer = []

    solutions = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            a = lines[i]
            b = lines[j]
            divided = a[0]*b[1] - a[1]*b[0]
            if divided == 0:
                continue
            x = (a[1]*b[2] - a[2]*b[1]) / divided
            y = (a[2]*b[0] - a[0]*b[2]) / divided
            if x == int(x) and y == int(y):
                solutions.append((int(x), int(y)))
    solutions.sort(key=lambda x: (x[0], x[1]))
    max_x, min_x, max_y, min_y = -INF, INF, -INF, INF
    for x, y in solutions:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    for _ in range(max_y - min_y + 1):
        answer.append("."*(max_x-min_x+1))
    for x, y in solutions:
        i = max_y - y
        j = abs(min_x - x)
        answer[i] = answer[i][:j]+"*"+answer[i][j+1:]
    return answer


if __name__ == "__main__":
    solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
