"""
- 연산자
연산자의 경우 내(현재 검사하는 연산자) 우선순위가 스택에 있는 연산자의 우선순위보다 같거나 낮으면,
스택에 있는 게 먼저 실행되어야 하므로 스택을 비우고 나를 넣는다.

- 괄호
괄호인 경우 '('는 일단 스택에 넣는다.
')'을 만나면 '('이 나올 때까지 스택을 다 비운다.

- 숫자
숫자의 경우 그냥 답에 넣는다
"""

exp = input()
stack = []  # 연산자들 저장하는 스택
prior = {'+': 1, '-': 1, '*': 2, '/': 2}
ans = ''
for oper in exp:
    if oper == '(':
        stack.append(oper)
    elif oper == ')':
        while len(stack) > 0 and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()  # '(' 비우기
    elif oper in prior:  # 연산자
        while len(stack) > 0 and stack[-1] != '(' and prior[stack[-1]] >= prior[oper]:
            if prior[stack[-1]] == '(':
                break
            ans += stack.pop()
        stack.append(oper)
    else:  # 숫자
        ans += oper
while len(stack) > 0 and stack[-1] != '(':  # 스택에 남은 것 비우기
    ans += stack.pop()
print(ans)
