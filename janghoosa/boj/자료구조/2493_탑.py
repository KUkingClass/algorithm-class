# 2493 탑
# https://www.acmicpc.net/problem/2493
N = int(input())
A = list(map(int, input().split()))
stack = []
ans = [0] * N
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]+1
    stack.append(i)
print(*ans)