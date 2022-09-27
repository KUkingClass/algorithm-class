import sys

"""
case1 실행시간: 2740ms
case2 실행시간: 148ms
"""
if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    # str_set = [sys.stdin.readline().strip() for _ in range(n)]   # case 1
    str_set = set(sys.stdin.readline().strip() for _ in range(n))  # case 2

    answer = 0
    for _ in range(m):
        if sys.stdin.readline().strip() in str_set:
            answer += 1

    print(answer)
