import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    city = list(map(int, sys.stdin.readline().split()))

    cache_right = [0 for _ in range(n)]     # 좌->우 방향 각 셀부터 끝까지 합 캐싱
    cache_right[0] = sum(city)
    for i in range(1, n):
        cache_right[i] = cache_right[i - 1] - city[i - 1]

    cache_left = [0 for _ in range(n)]      # 우->좌 방향 각 셀부터 끝까지 합 캐싱
    cache_left[-1] = cache_right[0]
    for i in range(n - 2, -1, -1):
        cache_left[i] = cache_left[i + 1] - city[i + 1]

    right = cache_right[0] - city[0]    # 꿀벌1과 벌통은 양끝에 위치
    answer = 0
    for i in range(1, n - 1):       # 꿀벌2 최적 위치 탐색
        answer = max(answer, right - city[i] + cache_right[i + 1])

    left = cache_left[-1] - city[-1]
    for i in range(n - 2, 0, -1):
        answer = max(answer, left - city[i] + cache_left[i - 1])

    answer = max(answer, sum(city[1:n//2 + 1]) + sum(city[n//2:-1]))    # 벌통이 중간에 위치
    print(answer)
