'''
https://www.acmicpc.net/problem/2493
탑

뒤에서부터 본다
내 전까지 아직 탑에 닿지 않은 신호들을 스택에 저장해둔다
만약 나보다 높이가 같거나 낮은 것들은 나한테 닿을 것
나한테 닿지 않은 것들은 모두 나보다 높이가 높다
그러니까 스택엔 높이가 높은 것부터 낮은 것 순으로 쌓여 있게 된다
'''

import sys

input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
ans = [0 for i in range(len(heights))]
untouched = []
for i in range(len(heights)-1, -1, -1):
    while len(untouched) > 0 and heights[untouched[-1]] <= heights[i]:
        ans[untouched[-1]]=i+1
        untouched.pop()
    untouched.append(i)
print(' '.join(map(str, ans)))
