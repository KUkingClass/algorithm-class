# 9012 괄호
# https://www.acmicpc.net/problem/9012
T = int(input())
for _ in range(T):
    A = list(input())
    qL = []
    qR = []
    cntL = cntR = 0
    flag = True
    for i in A:
        if i == '(':
            qL.append(i)
            cntL += 1
        if i == ')':
            qR.append(i)
            cntR += 1
        if qL and qR:
            qL.pop()
            qR.pop()
        if not qL and qR:
            flag = False
            break
    if flag and cntL==cntR:
        print('YES')
    else:
        print('NO')