# https://www.acmicpc.net/problem/20437
# 문자열 게임 2
# 30M
import sys

input = sys.stdin.readline
MAX_LIMIT = 10_005

test_case = int(input())
for t in range(test_case):
    word, k = input().strip(), int(input())
    min_ans, max_ans = MAX_LIMIT, 0
    for alpha_index in range(26):
        alpha = chr(ord('a')+alpha_index)
        indices = []
        for i in range(len(word)):
            if word[i] == alpha:
                indices.append(i)
        for i in range(k-1, len(indices)):
            length = indices[i]-indices[i-k+1]+1
            min_ans = min(min_ans, length)
            max_ans = max(max_ans, length)

    if min_ans == MAX_LIMIT:
        print(-1)
    else:
        print('{} {}'.format(min_ans, max_ans))
