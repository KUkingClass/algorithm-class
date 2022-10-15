n = int(input())
switches = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    
    if x == 1:
        num = y-1
        while num < n:
            switches[num] ^= 1
            num += y
    elif x == 2:
        switches[y-1] ^= 1
        left = y-2
        right = y
        while left>=0 and right < n and switches[left]==switches[right]:
            switches[left] ^= 1
            switches[right] ^= 1
            left -= 1
            right += 1

print(switches[0], end=' ')
for i in range(1, n):
    if i%20 == 0:
        print()
    print(switches[i], end=' ')

