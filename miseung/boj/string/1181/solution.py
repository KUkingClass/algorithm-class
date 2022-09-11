import sys

n = int(sys.stdin.readline())
list_set = list(set([input().strip() for _ in range(n)]))
list_set.sort(key=lambda x: (len(x), x))
for word in list_set:
    print(word)