# 10828 스택
# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    action = input().split()
    if action[0] == 'push':
        stack.append(action[1])
    elif action[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif action[0] == 'size':
        print(len(stack))
    elif action[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif action[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
        