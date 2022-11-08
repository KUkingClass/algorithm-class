n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]
tokens = []

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
new_d = [1, 0, 3, 2]
turns = 0
answer = -1

for i in range(k):
    token = list(map(lambda x: int(x) - 1, input().split()))
    board[token[0]][token[1]].append(i)
    tokens.append(token)

while turns < 1000:
    turns += 1

    for i, (r, c, d) in enumerate(tokens):
        indexes = []
        for temp_index in board[r][c]:
            if temp_index == i or len(indexes) > 0:
                indexes.append(temp_index)

        newr = r + dr[d]
        newc = c + dc[d]

        if newr < 0 or newr >= n or newc < 0 or newc >= n or grid[newr][newc] == 2:
            d = new_d[d]
            tokens[i][2] = d
            newr = r + dr[d]
            newc = c + dc[d]

        if newr < 0 or newr >= n or newc < 0 or newc >= n or grid[newr][newc] == 2:
            continue
        if grid[newr][newc] == 1:
            indexes.reverse()

        for temp_index in indexes:
            board[newr][newc].append(temp_index)
            board[r][c].pop(-1)
            tokens[temp_index][0] = newr
            tokens[temp_index][1] = newc

        if len(board[newr][newc]) >= 4:
            answer = turns
            break
    if answer >= 0:
        break

print(answer)
