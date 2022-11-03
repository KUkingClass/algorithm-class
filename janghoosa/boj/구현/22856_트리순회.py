# 22856 트리 순회
# https://www.acmicpc.net/problem/22856
import sys
from sys import stdin
sys.setrecursionlimit(10**8)
input = stdin.readline
N = int(input())
tree = [[] for _ in range(N)]
pdict = {}
for _ in range(N):
    n, a, b = map(int, input().split())
    tree[n-1] = [a-1,b-1]
    pdict[a-1] = n-1
    pdict[b-1] = n-1

visited = [False for _ in range(N)]
ans = []
def search(n):
    left, right = tree[n]
    if  left != -2 and not visited[left]:
        visited[left] = True
        search(left)
    ans.append(n)
    if right != -2 and not visited[right]:
        visited[right] = True
        search(right)

visited[0] = True
search(0)

visited = [False for _ in range(N)]
res = 0
visited[0] = True
n = 0
while True:
    left, right = tree[n]
    if  left != -2 and not visited[left]:
        visited[left] = True
        n = left
    elif right != -2 and not visited[right]:
        visited[right] = True
        n = right
    elif n == ans[-1]:
        break
    elif n in pdict:
        n = pdict[n]
    res += 1
print(res)