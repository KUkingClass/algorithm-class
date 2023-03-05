# 2580 스도쿠
# https://www.acmicpc.net/problem/2580
import sys
input = sys.stdin.readline
A = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if A[i][j] == 0:
            zero.append((i,j))

def check(x,y):
    checkfor = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if A[x][i] in checkfor:
            checkfor.remove(A[x][i])
        if A[i][y] in checkfor:
            checkfor.remove(A[i][y])
    nx = x//3*3
    ny = y//3*3
    for i in range(nx, nx+3):
        for j in range(ny,ny+3):
            if A[i][j] in checkfor:
                checkfor.remove(A[i][j])
    return checkfor
    
def dfs(n):
    if n == len(zero):
        for i in A:
            print(*i)
        exit(0)
    x, y = zero[n]
    res = check(x,y)
    for i in res:
        A[x][y] = i
        dfs(n+1)
        A[x][y] = 0
dfs(0)
