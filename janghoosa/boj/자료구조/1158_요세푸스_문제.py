# 1158 요세푸스 문제
# https://www.acmicpc.net/problem/1158
N, K = map(int, input().split())
A = [i for i in range(1,N+1)]
B = []
i = 0
while A:
    i += K-1
    while len(A) <= i:
        i -= len(A)
    B.append(str(A[i]))
    del A[i]
print("<",", ".join(B),">", sep="")