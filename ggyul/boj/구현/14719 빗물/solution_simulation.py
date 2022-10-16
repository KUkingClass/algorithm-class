'''
https://www.acmicpc.net/problem/14719
빗물
'''

h, w = map(int, input().split())
heights = map(int, input().split())
blocks = [[False]*(w+2) for _ in range(h+2)]
#맨 밑에 채워주기
for i in range(1, w+1):
    blocks[h+1][i] = True
for i, height in enumerate(heights):
    for j in range(height):
        blocks[h - j][i+1] = True
ans = 0

for i in range(h, 0, -1):
    start = 0
    for j in range(1, w+1):
        if blocks[i][j]:
            if start > 0:
                #물 다채움
                for water in range(start, j):
                    blocks[i][water] = True
                ans += j-start
                start = 0
        else:
            if start > 0:
                #바닥이 뚫려있으면..
                if not blocks[i+1][j]:
                    start = 0
            else:  # 새로 시작 가능?
                if blocks[i][j-1] and blocks[i+1][j]:
                    start = j


print(ans)
