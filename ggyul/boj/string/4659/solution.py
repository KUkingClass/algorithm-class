# https://www.acmicpc.net/problem/4659
# 비밀번호 발음하기
# 30M
import sys

input = sys.stdin.readline

vowels='aeiou'
twice_possible='eo'

def is_good(word):
    # 모음 하나 반드시 포함
    if not any(v in word for v in vowels):
        return False
    
    # 모음이나 자음 연속 3개 X
    for i in range(2, len(word)):
        # 다 True거나 다 False면 안됨
        if (word[i] in vowels)==(word[i-1] in vowels)==(word[i-2] in vowels):
            return False
        
    # 연속 2개 X
    for i in range(1, len(word)):
        if word[i] in twice_possible:
            continue
        if word[i] == word[i-1]:
            return False
    return True

ans=''
word = input().strip()
while word != 'end':
    if is_good(word):
        ans += '<'+word+'> is acceptable.\n'
    else:
        ans += '<'+word+'> is not acceptable.\n'
    word = input().strip()
print(ans)
