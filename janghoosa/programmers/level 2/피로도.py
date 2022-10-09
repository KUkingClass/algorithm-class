
# def solution(k, dungeons):

def dfs(n, k, dg, visit):
    print(n,k)
    max_dg = 0
    dfs = 0
    for idx in range(visit):
        if visit[idx] == -1 and dg[idx][0] <= k:
            max(dfs(n+1, k-dg[idx][1]), max_dg)
            dfs += 1
            k += dg[idx][1]
    if dfs == 0:
        return n
    return max_dg

k = int(input())
dugeons = input()
dg = sorted(dungeons, reverse=True)
visit = [-1] * len(dungeons)
answer = dfs(0, k, dg, visit)
print(answer)
# return answer