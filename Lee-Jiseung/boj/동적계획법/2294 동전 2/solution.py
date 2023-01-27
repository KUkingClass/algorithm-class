import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins = sorted(list(set(coins)))
counts = [10001] * (k+1)
counts[0] = 0
for coin in coins:
    if coin > k:
        break
    for i in range(coin, k+1):
        counts[i] = min(counts[i], 1 + counts[i-coin])
print(counts[k] if counts[k] != 10001 else -1)