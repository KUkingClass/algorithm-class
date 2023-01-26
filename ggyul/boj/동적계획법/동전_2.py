import sys

"""
합을 구할 수 없을 때 -1을 리턴하는 걸 안해줘서 틀렸다 ^^;
"""

INF = 100_005

n, k = map(int, input().split())
coins = list(set(int(sys.stdin.readline()) for _ in range(n)))
dp = [INF] * (k + 1)
dp[0] = 0
for value in range(len(dp)):
    for coin in coins:
        if value - coin < 0:
            continue
        dp[value] = min(dp[value], dp[value - coin] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
