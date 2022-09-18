n = int(input())
card = 2

while True:
    if n == 1 or n == 2:
        print(n)
        break
    card *= 2
    if card >= n:
        print((n - (card // 2)) * 2)
        break
