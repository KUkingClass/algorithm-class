n = int(input())
cnt = 0
for i in range(n):
    data = input()
    isOne = True
    for j in range(len(data) - 1):
        if data[j] != data[j + 1]:
            if data[j] in data[j + 1:]:
                isOne = False
                break
    if isOne:
        cnt += 1
print(cnt)
