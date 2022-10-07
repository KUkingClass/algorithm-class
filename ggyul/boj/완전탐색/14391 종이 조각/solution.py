'''
https://www.acmicpc.net/problem/14391
종이 조각
'''
m, n = map(int, input().split())
paper = [[] for _ in range(m)]
for i in range(m):
    paper[i] = list(map(int, list(input())))

max_ans = 0


def get_slice(index, is_sliced, ans):
    if index == m * n:
        global max_ans
        max_ans = max(max_ans, ans)
        return
    row, col = index // n, index % n
    if is_sliced[row][col] >= 0:
        get_slice(index + 1, is_sliced, ans)
    else:
        # 현재 조각 하나만
        is_sliced[row][col] = index
        get_slice(index + 1, is_sliced, ans + paper[row][col])
        is_sliced[row][col] = -1

        # 세로 조각
        for i in range(row + 1, m):
            if not any(is_sliced[j][col] >= 0 for j in range(row, i + 1)):
                added = 0
                for j in range(row, i + 1):
                    is_sliced[j][col] = index
                    added *= 10
                    added += paper[j][col]
                get_slice(index + 1, is_sliced, ans + added)
                for j in range(row, i + 1):
                    is_sliced[j][col] = -1
            else:
                break

        # 가로 조각
        for i in range(col + 1, n):
            if not any(is_sliced[row][j] >= 0 for j in range(col, i + 1)):
                added = 0
                for j in range(col, i + 1):
                    is_sliced[row][j] = index
                    added *= 10
                    added += paper[row][j]
                get_slice(index + 1, is_sliced, ans + added)
                for j in range(col, i + 1):
                    is_sliced[row][j] = -1
            else:
                break


is_slice = [[-1] * n for _ in range(m)]
get_slice(0, is_slice, 0)
print(max_ans)
