import sys
n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().strip()
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
