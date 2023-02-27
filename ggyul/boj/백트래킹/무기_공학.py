n, m = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]

ans = 0

visited = [[False] * m for _ in range(n)]

# 첫번째가 중심
shapes = [[(0, 1), (0, 0), (1, 1)], [(1, 1), (0, 1), (1, 0)], [(1, 0), (0, 0), (1, 1)], [(0, 0), (0, 1), (1, 0)]]


def is_other_empty(row, col, dx, dy, empty_count=3):
    x, y = row + dx, col + dy
    # 검사할 곳이 없으므로 그냥 false
    if not (0 <= x < n and 0 <= y < m) or not (x + 1 < n and y + 1 < m):
        return False
    return sum(not visited[x + i][y + j] for i in range(2) for j in range(2)) >= empty_count


def can_cut(shape):
    for x, y in shape:
        if not (0 <= x < n and 0 <= y < m) or visited[x][y]:
            return False
    return True


def cut(shape):
    value = 0
    for i, (x, y) in enumerate(shape):
        value += woods[x][y]
        if i == 0:
            value += woods[x][y]
    return value


def visit(shape, is_visited):
    for x, y in shape:
        visited[x][y] = is_visited


def get_shape(row, col, shape):
    return [(row + x, col + y) for x, y in shape]


def go(row, col, strength):
    if row == n:
        global ans
        ans = max(ans, strength)
        return
    if is_other_empty(row, col, -1, -2):
        return
    if col == m:
        go(row + 1, 0, strength)
        return
    # 현재 둘 수 있는 모양 4가지
    for shape in shapes:
        current_shape = get_shape(row, col, shape)
        if can_cut(current_shape):
            value = cut(current_shape)
            visit(current_shape, True)
            go(row, col + 1, strength + value)
            visit(current_shape, False)
    # 현재 지점 두지 않을려면 내 시작열과 내 왼쪽열이 비어있지 않을 때만 현재 지점을 두지 않음
    if is_other_empty(row, col, 0, -1, 4):
        return
    # 현재 지점 두지 않고 넘어가기
    go(row, col + 1, strength)


go(0, 0, 0)

print(ans)
