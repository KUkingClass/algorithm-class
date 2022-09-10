# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181
N = int(input())
A = [str(input()) for _ in range(N)]
A = sorted(A,key=lambda x:(len(x),x))
B = []
for i in A:
    if i not in B:
        B.append(i)
for i in B:
    print(i)