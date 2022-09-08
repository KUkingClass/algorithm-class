# https://www.acmicpc.net/problem/1316
n = int(input())
ans = 0
for case in range(n):
    word = input()
    prev = 0
    flag = True
    for i in range(len(word)):
        # 앞이랑 같으면 그냥 넘어감
        if i > 0 and word[i] == word[i-1]:
            continue
        # 앞이랑 다르면 이미 나온 문자인지 확인
        if prev & (1 << (ord(word[i])-ord('a'))):
            flag = False
            break
        prev |= 1 << (ord(word[i])-ord('a'))
    if flag:
        ans += 1
print(ans)
