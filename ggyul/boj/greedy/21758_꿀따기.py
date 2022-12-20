"""
https://www.acmicpc.net/problem/21758
꿀 따기

문제에서 '최대의 꿀의 양'으로 그리디 힌트를 주고 있다.
만약 벌통이 두 벌의 사이에 있는 경우가 아니라면,
무조건 벌통은 한 쪽 끝, 나머지 벌은 반대쪽이여야 가장 크다. 그리고 남은 벌의 위치에 따른 값을 계산한다.
그리고 벌통이 사이에 있을 경우를 따로 계산한다.

'두 수 사이의 값의 합'은 누적합을 통해 구한다.
"""

n = int(input())
honey_amounts = list(map(int, input().split()))
max_honey = 0

# 왼쪽 / 오른쪽 누적합
left_prefix = [0] * len(honey_amounts)
left_prefix[0] = honey_amounts[0]
for i in range(1, len(honey_amounts)):
    left_prefix[i] = left_prefix[i - 1] + honey_amounts[i]
right_prefix = [0] * len(honey_amounts)
right_prefix[-1] = honey_amounts[-1]
for i in range(len(honey_amounts) - 2, -1, -1):
    right_prefix[i] = right_prefix[i + 1] + honey_amounts[i]

# 1. 벌통이 사이에 있는 경우, 벌통 위치를 고른다
for i in range(1, len(honey_amounts) - 1):
    max_honey = max(max_honey, left_prefix[i] + right_prefix[i])
max_honey -= honey_amounts[0] + honey_amounts[-1]

# 2. 벌통이 왼쪽에 있는 경우
# 가장 왼쪽은 다른 벌, 가장 오른쪽은 벌통으로 이미 고정, 다른 벌 위치를 고른다
other_honey = left_prefix[-1] - left_prefix[0]
for i in range(1, len(honey_amounts) - 1):
    max_honey = max(max_honey, other_honey + left_prefix[-1] - left_prefix[i] - honey_amounts[i])

# 3. 벌통이 오른쪽에 있는 경우
# 위와 같다
other_honey = right_prefix[0] - right_prefix[-1]
for i in range(len(honey_amounts) - 2, 0, -1):
    max_honey = max(max_honey, other_honey + right_prefix[0] - right_prefix[i] - honey_amounts[i])

print(max_honey)
