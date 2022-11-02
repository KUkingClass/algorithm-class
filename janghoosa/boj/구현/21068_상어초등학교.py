# 21608 상어초등학교
# https://www.acmicpc.net/problem/21608
N = int(input())
M = [[0 for _ in range(N)]for _ in range(N)]
List = []
for _ in range(N*N):
    A = list(map(int, input().split()))
    T = A[0]
    B = A[1:]
    List.append([T, B])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in List:
    tmp = []
    # step1
    for y in range(N):
        for x in range(N):
            if M[y][x] == 0:
                blank = 0
                likes = 0
                for j in range(4):
                    if 0 <= dy[j]+y < N and 0<= dx[j]+x < N:
                        if M[dy[j]+y][dx[j]+x] == 0:
                            blank += 1
                        if M[dy[j]+y][dx[j]+x] in i[1]:
                            likes += 1
                tmp.append([likes, blank, y, x])
    tmp.sort(key= lambda x:(-x[0],-x[1],x[2],x[3]))
    M[tmp[0][2]][tmp[0][3]] = i[0]
ans = 0
for i in List:
    for y in range(N):
            for x in range(N):
                if M[y][x] == i[0]:
                    likes = 0
                    for j in range(4):
                        if 0 <= dy[j]+y < N and 0<= dx[j]+x < N:
                            if M[dy[j]+y][dx[j]+x] in i[1]:
                                likes += 1
                    if likes == 4:
                        ans += 1000
                    elif likes == 3:
                        ans += 100
                    elif likes == 2:
                        ans += 10
                    elif likes == 1:
                        ans += 1
print(ans)