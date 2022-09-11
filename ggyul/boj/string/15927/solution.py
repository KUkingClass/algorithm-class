# https://www.acmicpc.net/problem/15927
# 23분
"""
만약 어떤 단어가 회문이라고 해보자.
회문은 한 개만 붙이거나 빼면 회문이 아니게 된다.
그렇다면 이 문제에서는 맨 처음에 단어가 전체 회문인 지 아닌 지 검사 후에,
회문이라면 한 단어만 빼면 된다.
-> is_palindrome으로 검사

다만 주의할 것은 처음부터 끝까지 같은 글자로 이루어진 회문이라면 한 글자를 빼도 역시 회문이다.
따라서 전체가 같은 단어로 이루어졌는 지도 검사한다. (한 단어로 이루어졌을 때도 여기서 걸린다.)
-> is_all_same으로 검사
"""
word = input()
is_all_same = True
is_palindrome = True
lo, hi = 0, len(word)-1
while lo <= hi:
    if lo+1 < len(word) and word[lo] != word[lo+1]:
        is_all_same = False
    if word[lo] == word[hi]:
        lo+=1
        hi-=1
    else:
        is_palindrome = False
        break
if is_palindrome:
    if is_all_same:
        print(-1)
    else:
        print(len(word) - 1)
else:
    print(len(word))
