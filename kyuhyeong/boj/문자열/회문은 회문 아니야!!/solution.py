import sys


def solution(word):
    if len(set(word)) == 1:
        return -1

    limit = len(word)

    for i in range(limit // 2):
        if word[i] != word[limit - i - 1]:
            return limit

    return limit - 1


if __name__ == '__main__':
    word = sys.stdin.readline().strip()
    print(solution(word))
