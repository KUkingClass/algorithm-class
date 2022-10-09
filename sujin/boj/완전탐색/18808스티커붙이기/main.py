import sys

"""
   n, m (노트북 세로, 가로)
   k (스티커 개수)
"""

_input = sys.stdin.readline

# notebook info
notebook = [[]]
n = 0 # 세로
m = 0 # 가로


# 스티커 붙여보기
def stick(sticker):
    # 스티커 세로 가로
    r = len(sticker)
    c = len(sticker[0])

    for i in range(n):
        for j in range(m):
            is_stick = True
            for x in range(r):
                if not is_stick:
                    break
                for y in range(c):
                    if sticker[x][y] == 0:
                        continue
                    if i + x >= n or j + y >= m:  # 범위 벗어남
                        is_stick = False
                        break
                    if notebook[i + x][j + y]:  # 이미 스티커 붙여져있음
                        is_stick = False
                        break
            if is_stick:  # 스티커 붙일 수 있음
                for k in range(r):
                    for w in range(c):
                        if sticker[k][w] == 0:
                            continue
                        notebook[i + k][j + w] = True  # 붙인다
                return True
    return False


# 스티커 회전하기
def rotate(sticker):
    return [list(row) for row in zip(*sticker[::-1])]


if __name__ == '__main__':
    answer = 0
    (_n, _m, k) = map(int, _input().strip().split())

    notebook = [[False for _ in range(_m)] for _ in range(_n)]  # 노트북
    n = _n
    m = _m

    for _ in range(k):  # 스티커 k개
        (r, c) = map(int, _input().strip().split())
        sticker = [[0 for _ in range(c)] for _ in range(r)]  # r x c 2차원 배열

        for i in range(r):
            sticker[i] = list(map(int, _input().strip().split()))

        print(sticker)

        rotate_cnt = 0
        while rotate_cnt < 4:
            if stick(sticker):  # 스티커 붙이면 break
                break
            rotate(sticker)  # 안맞으면 회전

    for i in range(n):
        for j in range(m):
            if notebook[i][j]:
                answer += 1

    print(answer)
