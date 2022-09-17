'''
https://www.acmicpc.net/problem/2800
괄호 제거
괄호 쌍은 최대 10개이므로 10! == 3628800

괄호가 몇 번째 괄호인지 저장해두고,
하나씩 지워가면서
모든 경우의 수를 보기만 하면 된다
'''
exp = input().strip()

# 한 괄호쌍이 어디 어디에 있는 지 알면 된다
brackets = []
stack = []
for i in range(len(exp)):
    if exp[i]=='(':
        stack.append(i)
    elif exp[i] == ')':
        brackets.append([stack.pop(), i])

ans = []

def erase(index, is_bracket_erased):
    if index==len(brackets): # 모두 체크 완료
        # 모두 안지우는 경우는 뺀다
        if all(erased==False for erased in is_bracket_erased):
            return
        erased = [False for _ in range(len(exp))]
        for i in range(len(brackets)):
            if is_bracket_erased[i]:
                erased[brackets[i][0]]=True
                erased[brackets[i][1]] = True
        erased_exp =''
        for i in range(len(exp)):
            if not erased[i]:
                erased_exp+=exp[i]
        ans.append(erased_exp)
        return
    is_bracket_erased[index] = False
    erase(index+1, is_bracket_erased)
    is_bracket_erased[index]=True
    erase(index+1, is_bracket_erased)

is_bracket_erased = [False for _ in range(len(brackets))]
erase(0, is_bracket_erased)
ans.sort()
for i in range(len(ans)):
    if i > 0 and ans[i]==ans[i-1]:
        continue
    print(ans[i])