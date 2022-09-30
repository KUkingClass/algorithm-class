import sys
from collections import deque

if __name__ == '__main__':
    _input = sys.stdin.readline

    n = int(_input())
    deque = deque()

    for i in range(n):
        comm = _input().strip().split()
        oper = comm[0]

        if oper == 'push_front':
            deque.appendleft(comm[1])

        elif oper == 'push_back':
            deque.append(comm[1])

        elif oper == 'pop_front':
            print(deque.popleft() if deque else -1)

        elif oper == 'pop_back':
            print(deque.pop() if deque else -1)

        elif oper == 'size':
            print(len(deque))

        elif oper == 'empty':
            print(1 if not deque else 0)

        elif oper == 'front':
            print(deque[0] if deque else -1)

        elif oper == 'back':
            print(deque[len(deque)-1] if deque else -1)
