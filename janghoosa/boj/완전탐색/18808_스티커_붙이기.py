# 18808 스티커 붙이기
# https://www.acmicpc.net/problem/18808
N, M, K = map(int, input().split())
NBook = [[0] * M for _ in range(N)]
Blocks = []

def rotated(arr):
    return [list(elem) for elem in zip(*arr[::-1])]

def fitin(NBook, Block ,x, y):
    for i in range(len(Block)):
        for j in range(len(Block[0])):
            if Block[i][j]:
                if NBook[x+i][y+j] == 1:
                    return False
    return True

def place_block(NBook, block, n):
    if n == 4:
        return
    bx = len(block)
    by = len(block[0])
    if N < bx or M < by:
        place_block(NBook, rotated(block),n+1)
        return
    for i in range(N-bx+1):
        for j in range(M-by+1):
            if fitin(NBook, block, i, j):
                for k in range(bx):
                    for l in range(by):
                        if block[k][l]:
                            NBook[i+k][j+l] = 1
                return
    place_block(NBook, rotated(block),n+1)

for _ in range(K):
    row, col = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(row)]
    Blocks.append(A)


for Block in Blocks:
    place_block(NBook, Block, 0)
print(sum(map(sum, NBook)))