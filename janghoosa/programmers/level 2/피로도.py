answer = 0
N = 0
visited = []

def dfs(k, cnt, dg):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dg[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dg[j][1], cnt + 1, dg)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
