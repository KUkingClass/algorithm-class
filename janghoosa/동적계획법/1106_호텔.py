C, N = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

dp = [1000001] * (C+100)
dp[0] = 0

for cost, people in city:
    for i in range(people, C+100):
        dp[i] = min(dp[i-people]+cost, dp[i])

print(min(dp[C:]))