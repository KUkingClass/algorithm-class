# 6443 애너그램
# https://www.acmicpc.net/problem/6443
import sys
input = sys.stdin.readline
	 
def solve(word, temp):
    global ans
    if len(word) == len(temp):
        print(temp)
        return
    else:
        for i in range(len(word)):
            if not visited[i]:
                temp2 = temp + word[i]
                if temp2 not in record:
                    record.add(temp2)
                    visited[i] = True
                    solve(word, temp2)
                    visited[i] = False

N = int(input())
for _ in range(N):
    word = list(input().strip())
    word.sort()
    visited = [False]*len(word)
    record = set()
    solve(word, '')