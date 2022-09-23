import re


def trans_digit(n, k):
    answer = []
    while n:
        n, remainder = divmod(n, k)
        answer.append(remainder)

    return "".join(map(str, answer[::-1]))


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    transformed = trans_digit(n, k)
    split = map(int, filter(lambda x: x, re.split("(0)+", transformed)))
    return len(list(filter(lambda x: is_prime(x), split)))


if __name__ == '__main__':
    n, k = 437674, 3
    # n, k = 110011, 10
    # n, k = 1000000, 9
    print(solution(n, k))
