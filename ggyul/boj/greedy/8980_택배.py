"""
어쨌든 **빨리 내릴 수 있는 거** 싣는 게 이득
그 전 풀이 아이디어도 >>지금 이 순간 빨리 내릴 수 있는거 선택하자<< 였는데
왜 틀린지 모르겠어서 찾아보고 풀었다 ^..^ 아마 중간 용량을 잘못 확인한 것 같음
"""
import sys

input = sys.stdin.readline
n, c = map(int, input().split())  # 마을 수, 트럭의 용량
m = int(input())
from_to = [tuple(map(int, input().split())) for _ in range(m)]
from_to.sort(key=lambda x: x[1])
# 각 마을에 도착할 때 남은 용량
remain = [c] * n
max_count = 0
# M * N
for start, end, count in from_to:
    possible_count = min(count, min(remain[start:end]))
    max_count += possible_count
    for i in range(start, end):
        remain[i] -= possible_count
    print(remain)
print(max_count)
