# 22942 데이터 체커
# https://www.acmicpc.net/problem/22942
import sys
input = sys.stdin.readline
N = int(input())
circle = []
stack = []
for i in range(N):
    x, r = map(int, input().split())
    circle.append([x-r,0,i])
    circle.append([x+r,1,i])
circle.sort()
for i in range(2*N):
    dir = circle[i][1]
    if dir == 0:
        stack.append(circle[i])
    else:
        if stack[-1][1] == 0:
            if stack[-1][2] == circle[i][2]:
                stack.pop()
            else:
                print("NO")
                exit(0)
print("YES")
