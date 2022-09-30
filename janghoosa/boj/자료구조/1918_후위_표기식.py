# 1918 후위 표기식
# https://www.acmicpc.net/problem/1918
A = input()
stack = []
ans = ''
for i in A:
    if i.isalpha():
        ans += i
    else:
        if i =='(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i =='-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)