import sys

n = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

prices = [0] * (n+1)
max_price = 0
for i, (t, p) in enumerate(infos):
    max_price = max(max_price, prices[i])
    prices[i] = max_price
    if i + t > n:
        continue
    prices[i+t] = max(prices[i+t], prices[i] + p)
print(max(prices))