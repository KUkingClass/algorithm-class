n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]

result = []
count = 0

for i in range(n):
    count += k - 1
    if count >= len(arr):
        count = count % len(arr)
    result.append(str(arr.pop(count)))
print("<", ", ".join(result), ">", sep='')
