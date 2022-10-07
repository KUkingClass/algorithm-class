'''
https://www.acmicpc.net/problem/18808
스티커 붙이기
'''
import sys


n, m, k = map(int, input().split())
stickers = []
notebook = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for i in range(r):
        sticker.append(list(map(int, input().split())))
    stickers.append(sticker)


def rotate(sticker):
    rotated = [[0] * len(sticker) for _ in range(len(sticker[0]))]
    for i in range(len(sticker)):
        for j in range(len(sticker[i])):
            rotated[j][len(sticker)-1-i] = sticker[i][j]
    return rotated


def attach_if_possible(sticker):
    for i in range(0, len(notebook)-len(sticker)+1):
        for j in range(0, len(notebook[0])-len(sticker[0])+1):
            # 이 좌표를 시작으로 붙일 수 있는지
            is_attachable = True
            for m in range(len(sticker)):
                for n in range(len(sticker[0])):
                    if sticker[m][n] == 1 and notebook[i+m][j+n] == 1:
                        is_attachable = False
                        break
                if not is_attachable:
                    break
            if is_attachable:
                for m in range(len(sticker)):
                    for n in range(len(sticker[0])):
                        if sticker[m][n] == 1:
                            notebook[i+m][j+n] = 1
                return True
    return False


def attach(sticker):
    for i in range(4):
        if i != 0:
            # sticker = list(zip(*sticker[::-1]))
            sticker = rotate(sticker)
        is_attached = attach_if_possible(sticker)
        if is_attached:
            return


for sticker in stickers:
    is_attached = attach(sticker)
ans = 0
for i in range(len(notebook)):
    for j in range(len(notebook[i])):
        ans += notebook[i][j]
print(ans)
