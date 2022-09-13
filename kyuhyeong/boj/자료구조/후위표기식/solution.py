import sys

if __name__ == '__main__':
    infix = sys.stdin.readline().strip()
    postfix = ""
    stack = []

    for ch in infix:
        if 'A' <= ch <= 'Z':
            postfix += ch
        elif ch in ['*', '/']:
            if stack and stack[-1] in ['*', '/']:
                postfix += stack.pop()
            stack.append(ch)
        elif ch in ['+', '-']:
            while stack and stack[-1] in ['*', '/', '+', '-']:
                postfix += stack.pop()
            stack.append(ch)
        elif ch == '(':
            stack.append(ch)
        else:  # case ')'
            while True:
                top = stack.pop()
                if top == '(':
                    break
                postfix += top

    while stack:
        postfix += stack.pop()

    print(postfix)
