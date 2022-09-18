# 15927 회문은 회문아니야!!
# https://www.acmicpc.net/problem/15927
A = input()
B = A[:-1]

def check(x):
    if x == x[::-1]:
        return 0
    return 1
if check(A):
    print(len(A))
elif check(B):
    print(len(B))
else:
    print(-1)