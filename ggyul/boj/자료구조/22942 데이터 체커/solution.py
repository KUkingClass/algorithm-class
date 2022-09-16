'''
# https://www.acmicpc.net/problem/22942
# 데이터 체커

다 탐색하는 거 말고 생각을 못하겠어서 검색했다가
처음엔 스위핑 느낌으로 풀려고 했다가 실패
그랬다가 올바른 괄호 문자열처럼
()(()) 같이 생각하라는 힌트 보고 풀었다
sort하므로 O(NlogN)
N=200,000이므로 N^2시에 10^10이므로 불가능 (10^7정도 까지만 가능)
'''

import sys
input = sys.stdin.readline
n = int(input())
points = []  # n번째 원, '('인지 여부, 좌표
for i in range(n):
    x, r = map(int, input().split())
    points.append(tuple([i, True, x-r]))
    points.append(tuple([i, False, x+r]))
points.sort(key=lambda x: x[2])  # 좌표 기준 정렬

stack = []  # 열린 원들만 저장해도 됨
is_right = True
for point in points:
    if point[1]:  # '('일 때
        stack.append(point)
    else:  # ')'일 때
        if stack[-1][0] != point[0]:  # 다른 원임 -> 짝이 안맞음
            is_right = False
            break
        stack.pop()
if is_right:
    print('YES')
else:
    print('NO')
