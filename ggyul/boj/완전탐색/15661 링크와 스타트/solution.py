n = int(input())
ablities = [list(map(int, input().split())) for _ in range(n)]
ans = 500
for mask in range(3, (1 << (n-1)) - 1):
    teams = [[], []]
    for i in range(n):
        if (1 << i) & mask:
            teams[1].append(i)
        else:
            teams[0].append(i)
    score = [0, 0]
    for num, team in enumerate(teams):
        for i in range(len(team)):
            for j in range(len(team)):
                score[num] += ablities[team[i]][team[j]]
    ans = min(ans, abs(score[0]-score[1]))
print(ans)
