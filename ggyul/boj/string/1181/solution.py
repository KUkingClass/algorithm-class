# https://www.acmicpc.net/problem/1181
import sys

input = sys.stdin.readline

n = int(input())
li_set = set([input().strip() for _ in range(n)])
li = list(li_set)
li.sort(key=lambda x: (len(x), x))
for word in li:
    print(word)
