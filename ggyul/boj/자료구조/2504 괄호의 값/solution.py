# https://www.acmicpc.net/problem/2504
# 괄호의 값
exp = input()

opened = {')': '(', ']': '['}


def validate():
    open_counts = {'(': 0, '[': 0}
    for s in exp:
        if s in open_counts:  # open 인 경우
            open_counts[s] += 1
        else:
            if open_counts[opened[s]] <= 0:
                return False
            open_counts[opened[s]] -= 1
    if any(open_counts[i] > 0 for i in open_counts):
        return False
    return True


values = {'(': 2, '[': 3}
closed = {'(': ')', '[': ']'}

'''
return: value, next_start
재귀함수로, 현재 시작하는 지점의 괄호가 끝나는 지점까지 계산해서,
현재 괄호 계산 값과 다음 시작할 인덱스를 리턴한다
'''
def calculate(start):
    # 현재 괄호 안에 아무것도 없음
    if exp[start+1] == closed[exp[start]]:
        return values[exp[start]], start+2
    sum = 0
    i = start+1
    while i < len(exp):
        if exp[i] == '(' or exp[i] == '[':
            value, next_start = calculate(i)
            sum += value
            i = next_start
        else:
            # 현재 괄호 끝남
            return values[exp[start]]*sum, i+1


if not validate():
    print('0')
else:
    sum = 0
    i = 0
    while i < len(exp):
        added, i = calculate(i)
        sum += added
    print(sum)
