n = int(input())
ans = 0
for i in range(n):
    word = list(input())
    check = []
    prev = ''
    isGroup = True
    for j in word:
        if prev != j:
            if j in check:
                isGroup = False
                break
            else:
                prev = j
                check.append(j)
    if isGroup:
        ans += 1
print(ans)