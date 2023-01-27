import sys

c, n = map(int, sys.stdin.readline().split())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
clients = [0] * (1000*101)
for cost, client in costs:
    for i in range(cost, 1000*101):
        clients[i] = max(clients[i], clients[i-cost] + client)

for i, client in enumerate(clients):
    if client >= c:
        print(i)
        break
