# https://www.acmicpc.net/problem/10828
# 스택
import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    opers = input().strip().split()
    oper = opers[0]
    if oper == 'push':
        stack.append(opers[1])
    elif oper == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif oper == 'size':
        print(len(stack))
    elif oper == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif oper == 'top':
        print(stack[-1] if len(stack) > 0 else -1)
