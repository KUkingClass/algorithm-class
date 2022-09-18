import sys
from collections import deque

# 1..N 풍선 원형
# 종이에 -N..N 중의 정수 1개 적혀있음
# 제일 처음 1번 터뜨림
# 풍선 안에 종이에 적힌 값만큼 이동
# 양수면 오른쪽 음수는 왼쪽
# 이미 터진 풍선 제외

# enumerate
# (idx, val) pair 형태

if __name__ == '__main__':
    _input = sys.stdin.readline

    n = int(_input())
    balloon = deque(enumerate(map(int, input().split())))
    result = []

    # 3 2 1 -3 -1

    # 2 1 -3 -1 pop
    # -3 -1 2 1 left rot

    # -1 2 1 pop
    # -1 2 1 right rot

    for i in range(n):
        (idx, num) = balloon.popleft()
        result.append(idx + 1)

        if num > 0:
            # 이미 pop 했기 때문에 num-1만큼 왼쪽으로 회전(오른쪽 이동)
            balloon.rotate(-(num-1))
        else:
            balloon.rotate(-num)

    print(' '.join(map(str, result)))