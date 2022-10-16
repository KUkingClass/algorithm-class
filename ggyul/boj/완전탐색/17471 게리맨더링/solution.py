'''
https://www.acmicpc.net/problem/17471
게리맨더링
'''


n = int(input())
population = list(map(int, input().split()))
population_sum = sum(population)

graph = [[-1]]
for i in range(n):
    num, *adjacency = map(int, input().split())
    graph.append(adjacency)

ans = 1005


def solution(mask):
    teams = [[], []]
    for i in range(n):
        if (1 << i) & mask:
            teams[1].append(i+1)
        else:
            teams[0].append(i+1)
    # Team0, 1 가능한 경우인지 확인
    for team in teams:
        stack = []
        visited = [False]*(n+1)
        stack.append(team[0])
        while len(stack) > 0:
            top = stack.pop()
            visited[top] = True
            for num in graph[top]:
                if num in team and not visited[num]:
                    stack.append(num)
        if any(not visited[num] for num in team):
            return
    #가능함 -> 인구수 계산
    popl = 0
    for num in teams[0]:
        popl += population[num-1]
    rest_popl = population_sum - popl
    global ans
    ans = min(ans, abs(popl-rest_popl))


for mask in range(1, (1 << (n-1))+1):
    solution(mask)

print(ans) if ans != 1005 else print(-1)
