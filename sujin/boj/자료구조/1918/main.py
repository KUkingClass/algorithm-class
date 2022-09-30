import sys

# a*(b+c) a *
# a*bc+
# abc+*

'''
알파벳
결과에 추가 해주면 됨

연산자
*/ 이면 +- 빼고 추가
+- 이면 내가 제일 낮으므로 모두 추가

괄호
'('는 스택에 넣고, ')'이면 '('를 만날 때까지 pop
'''

if __name__ == '__main__':
    _input = sys.stdin.readline

    equ = _input().strip()

    stack = []
    result = ''

    for op in equ:

        if op.isalpha():
            # 알파벳
            result += op

        elif op == '+' or op == '-':
            while stack and stack[-1] in ['+', '-', '*', '/']:
                result += stack.pop()
            stack.append(op)

        elif op == '*' or op == '/':
            while stack and stack[-1] in ['*', '/']:
                result += stack.pop()
            stack.append(op)

        elif op == '(':
            stack.append(op)

        elif op == ')':
            while True:
                p = stack.pop()
                if p == '(':
                    break
                else:
                    result += p

    # 남은 스택 비우기
    while stack:
        result += stack.pop()

    print(result)