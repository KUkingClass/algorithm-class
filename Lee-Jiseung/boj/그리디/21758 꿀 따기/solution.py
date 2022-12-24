import sys

n = int(sys.stdin.readline())
amounts = list(map(int, sys.stdin.readline().split()))

total = sum(amounts)
answer = total-amounts[0]-amounts[-1]+max(amounts[1:n])

first = total - amounts[0]
second = total - amounts[0]
for i in range(1, n-1):
    second -= amounts[i]
    answer = max(answer, first + second - amounts[i])
    
first = total - amounts[-1]
second = total - amounts[-1]
for i in range(n-2, 0, -1):
    second -= amounts[i]
    answer = max(answer, first + second - amounts[i])
print(answer)
