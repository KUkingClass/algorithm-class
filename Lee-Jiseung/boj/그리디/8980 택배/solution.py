import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
infos = sorted(infos, key=lambda x (x[0], x[1]))

answer = 0
capacity = [0]  (n+1)
truck = 0
for start, end, quantity in infos
    for i in range(1, start+1)
        truck -= capacity[i]
        answer += capacity[i]
        capacity[i] = 0

    capacity[end] += quantity
    truck += quantity

    i = n
    while truck  c
        remove = min(truck -c, capacity[i])
        truck -= remove
        capacity[i] -= remove
        i -= 1

print(answer + sum(capacity))