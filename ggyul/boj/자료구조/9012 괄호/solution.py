# https://www.acmicpc.net/problem/9012
# 괄호
import sys
test_case = int(input())
for t in range(test_case):
    input_string = sys.stdin.readline().strip()
    opened_count = 0
    is_right = True
    for s in input_string:
        if s == '(':
            opened_count += 1
        elif s == ')':
            if opened_count == 0:
                is_right = False
                break
            opened_count -= 1
    if opened_count != 0:
        is_right = False
    print('YES') if is_right else print('NO')
