# 1969 DNA
# https://www.acmicpc.net/problem/1969
N, M = map(int, input().split())
A = [input() for _ in range(N)]
ans = ''
cnt = 0
for i in range(M):
    B = [0] * 4
    for j in range(N):
        if A[j][i] == 'A':
            B[0] += 1
        elif A[j][i] == 'C':
            B[1] += 1
        elif A[j][i] == 'G':
            B[2] += 1
        elif A[j][i] == 'T':
            B[3] += 1
    idx = B.index(max(B))
    if idx == 0:
        ans += 'A' 
    elif idx == 1:
        ans += 'C'
    elif idx == 2:
        ans += 'G'
    elif idx == 3:
        ans += 'T'
    cnt += N - max(B)
print(ans)
print(cnt)