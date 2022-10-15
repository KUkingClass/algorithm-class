h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(h):
    left = -1
    for j in range(w):
        if blocks[j] > i:
            if left >= 0:
                answer += j - left - 1
            left = j
            continue

print(answer)