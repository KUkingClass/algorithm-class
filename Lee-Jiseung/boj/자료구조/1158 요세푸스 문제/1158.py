n,k = input().split()
n = int(n)
k = int(k)
cl = [i for i in range(1, n+1)]

print('<', end='')
idx = k-1
for _ in range(n - 1):
    print(str(cl[idx])+',', end=' ')
    cl.pop(idx%len(cl))
    idx += k-1
    idx = idx%len(cl)
print(cl[0], end='')
print('>', end='')