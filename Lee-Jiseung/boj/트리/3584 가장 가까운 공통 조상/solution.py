import sys

T = int(sys.stdin.readline())
for test_case in range(T):
    N = int(sys.stdin.readline())
    edges = [-1] * N
    for _ in range(N-1):
        A, B = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        edges[B] = A
        
    A, B = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    ancestor_A = [-1, A]
    while True:
        A = edges[A]
        if A == -1:
            break
        ancestor_A.append(A)
    ancestor_B = [-2, B]
    while True:
        B = edges[B]
        if B == -1:
            break
        ancestor_B.append(B)
        
    answer= -1
    while ancestor_A[answer] == ancestor_B[answer]:
        answer -= 1
    print(ancestor_B[answer + 1] + 1)