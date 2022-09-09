# 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
N = int(input())
ans = 0
for _ in range(N):
    A = list(input())
    i = 0
    dic = {}
    while i < len(A):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            break
        while i+1 < len(A) and A[i+1] == A[i] :
            i += 1
        if i == len(A)-1:
            ans += 1
        i += 1
print(ans)