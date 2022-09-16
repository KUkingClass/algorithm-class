import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for i in range(n):
        phesis = sys.stdin.readline()

        isVps = True
        stack = []

        for s in phesis:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if stack:
                    # 스택에 '(' 가 있을 때
                    stack.pop()
                else:
                    # 빈 스택
                    isVps = False
                    break

        # for문이 끝까지 수행(break로 안끊기고) 됐을 때
        # stack이 비어 있지 않으면 짝이 안맞는 괄호 남은 것
        else:
            if stack:
                isVps = False

        print("YES" if isVps else "NO")