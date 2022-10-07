def solution(n, left, right):
    answer = [0 for _ in range(right - left + 1)]

    for idx, num in enumerate(range(left, right + 1)):
        i, j = divmod(num, n)
        answer[idx] = max(i, j) + 1

    return answer


if __name__ == '__main__':
    n, left, right = 4, 7, 14
    print(solution(n, left, right))
