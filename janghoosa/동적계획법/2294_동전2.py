N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))
    
dp = [10001] * (K+1)
dp[0] = 0

for c in coin:
    for i in range(c,K+1):
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])