# https://www.acmicpc.net/problem/10866
# 덱
import sys

li = [0 for _ in range(30_005)]
front = 10_000 # 지금 값이 있는 가장 앖
back = 10_000 # 이제 값이 들어갈 곳

def is_empty():
    return True if back == front else False

n = int(input())
for _ in range(n):
    oper = sys.stdin.readline().split()
    if oper[0]=='push_front':
        front -= 1
        li[front] = oper[1]
    elif oper[0] == 'push_back':
        li[back] = oper[1]
        back+=1
    elif oper[0] == 'pop_front':
        if is_empty():
            print(-1)
        else:
            print(li[front])
            front+=1
    elif oper[0] == 'pop_back':
        if is_empty():
            print(-1)
        else:
            print(li[back-1])
            back-=1
    elif oper[0] == 'size':
        print(0) if is_empty() else print(back-front)
    elif oper[0] == 'empty':
        print(1) if is_empty() else print(0)
    elif oper[0] == 'front':
        print(-1) if is_empty() else print(li[front])
    elif oper[0] == 'back':
        print(-1) if is_empty() else print(li[back-1])
