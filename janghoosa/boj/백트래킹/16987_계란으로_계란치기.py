# 16987 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
res = 0

def solve(idx):
    global res
    if idx == N:
        brokeneggs = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                brokeneggs += 1
        res = max(res, brokeneggs)
        return

    if eggs[idx][0] <= 0:
        solve(idx+1)
        return
    
    isAllBroken = True
    for target in range(N):
        if target == idx:
            continue
        if eggs[target][0] > 0:
            isAllBroken = False
            break
    if isAllBroken:
        res = max(res, N-1)
        return
    
    for target in range(N):
        if target == idx:
            continue
        if eggs[target][0] <= 0:
            continue
        
        eggs[idx][0] -= eggs[target][1]
        eggs[target][0] -= eggs[idx][1]
        solve(idx+1)
        eggs[idx][0] += eggs[target][1]
        eggs[target][0] += eggs[idx][1]

solve(0)
print(res)