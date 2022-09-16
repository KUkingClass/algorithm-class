import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    stack = []

    for i in range(n):
        comm = sys.stdin.readline().strip().split()
        oper = comm[0]

        if oper == 'push':
            stack.append(comm[1])
        elif oper == 'pop':
            print(stack.pop() if stack else -1)
        elif oper == 'top':
            print(stack[-1] if stack else -1)
        elif oper == 'empty':
            print(1 if not stack else 0)
        elif oper == 'size':
            print(len(stack))