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


# 스티커 회전하기
def rotate(sticker):
    return [list(row) for row in zip(*sticker[::-1])]


# 붙일 수 있는 자리인지
def is_stick(sticker, x, y):
    # 스티커 세로 가로
    r = len(sticker)
    c = len(sticker[0])

    for i in range(r):
        for j in range(c):
            if x + i >= n or y + j >= m:
                return False
            elif sticker[i][j] == 1 and notebook[x + i][y + j]:
                return False
    return True


# 스티커 붙여보기
def stick(sticker):
    # 스티커 세로 가로
    r = len(sticker)
    c = len(sticker[0])

    # notebook 순회 시작
    for i in range(n):
        for j in range(m):
            if is_stick(sticker, i, j): # 불일 수 있으면 붙인다
                for x in range(r):
                    for y in range(c):
                        if sticker[x][y] == 0:
                            continue
                        notebook[i + x][j + y] = True  # 붙인다
                return True
    return False


if __name__ == '__main__':
    answer = 0
    (_n, _m, k) = map(int, _input().strip().split())

    # 노트북 정보 생성
    notebook = [[False for _ in range(_m)] for _ in range(_n)]
    n = _n
    m = _m

    for _ in range(k):  # 스티커 k개
        (r, c) = map(int, _input().strip().split())
        sticker = [[0 for _ in range(c)] for _ in range(r)]  # r x c 2차원 배열

        for i in range(r):
            sticker[i] = list(map(int, _input().strip().split()))

        rotate_cnt = 0
        while rotate_cnt < 4:
            if stick(sticker):  # 스티커 붙이면 break
                break
            sticker = rotate(sticker)  # 안맞으면 회전
            rotate_cnt += 1

    # 스티커 붙여져 있는 칸 세기
    for i in range(n):
        for j in range(m):
            if notebook[i][j]:
                answer += 1

    print(answer)
