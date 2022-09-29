n, m = map(int, input().split(' '))
dna = [input() for _ in range(n)]

answer = ""
hd = 0
count = [[0 for _ in range(4)] for _ in range(m)]

for i in range(m):
    count = {"A":0, "C":0, "G":0, "T":0}
    for d in dna:
        count[d[i]] += 1
    count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    answer += count[0][0]
    hd += n - count[0][1]

print(answer)
print(hd)