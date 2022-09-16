import sys

if __name__ == '__main__':
    _input = sys.stdin.readline
    n = int(_input())

    queue = []
    pointer = 0 # pop() 하면 시간초과, pointer로 pop 위치 지정
    for i in range(n):
        comm = _input().strip().split()
        oper = comm[0]
        curSize = len(queue) - pointer

        if oper == 'push':
            queue.append(comm[1])

        elif oper == 'pop':
            if curSize > 0:
                print(queue[pointer])
                pointer += 1 # 정상적 pop이 됐을 때만 +1
            else:
                print(-1)

        elif oper == 'size':
            print(curSize)

        elif oper == 'empty':
            print(1 if curSize == 0 else 0)

        elif oper == 'front':
            print(queue[pointer] if curSize > 0 else -1)

        elif oper == 'back':
            print(queue[-1] if curSize > 0 else -1)
