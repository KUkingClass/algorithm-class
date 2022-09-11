# https://www.acmicpc.net/problem/17609
# 회문 (유사 회문)
# 30M
# 투포인터로 두 글자가 다르다면 왼쪽, 오른쪽 각각 점프
import sys
input = sys.stdin.readline

PALINDROME = 0
PSEUDO = 1
NOT_ALL = 2


def is_palindrome(word, lo, hi, jumped):
    while lo <= hi:
        if word[lo] == word[hi]:
            lo += 1
            hi -= 1
            continue
        if jumped:
            return NOT_ALL
        # 왼쪽 점프
        return PSEUDO if (is_palindrome(word, lo+1, hi, True) == PSEUDO
                          or is_palindrome(word, lo, hi-1, True)) == PSEUDO else NOT_ALL
    return PSEUDO if jumped else PALINDROME


test_case = int(input())
for t in range(test_case):
    word = input().strip()
    print(is_palindrome(word, 0, len(word)-1, False))
