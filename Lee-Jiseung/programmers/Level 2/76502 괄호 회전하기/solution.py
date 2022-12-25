bracket = {')':'(', '}':'{', ']':'[', '(':-1, '{':-1, '[':-1}

def is_correct(s):
    stack = []
    for c in s:
        if bracket[c] != -1:
            if stack and stack[-1] == bracket[c]:
                stack.pop()
            else:
                return 0
        else:
            stack.append(c)
    if stack:
        return 0
    return 1


def rotate(s):
    return s[1:]+s[0]


def solution(s):
    answer = 0
    for _ in range(len(s)):
        answer += is_correct(s)
        s = rotate(s)
    return answer
