# 4659 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
vowel = ['a','i','e','o','u']
while True:
    word = input()
    if word == 'end':
        break
    check1 = False
    for i in vowel:
        if i in word:
            check1 = True
            break
    check2 = True
    i=0
    while i < len(word):
        strick = 0
        strick2 = 0
        if word[i] in vowel:
            strick += 1
            while i < len(word):
                i += 1
                if i == len(word):
                    break
                if word[i] in vowel:
                    strick += 1
                else:
                    i -= 1
                    break
                if strick >= 3:
                    check2 = False
                    break
        else:
            strick2 += 1
            while i < len(word):
                i += 1
                if i == len(word):
                    break
                if word[i] not in vowel:
                    strick2 += 1
                else:
                    i -= 1
                    break
                if strick2 >= 3:
                    check2 = False
                    break
        if check2 == False:
            break
        i+=1
    check3 = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] == 'o' or word[i] =='e':
                break
            else:
                check3 = False
    if check1 and check2 and check3:
        print('<'+word+'> is acceptable.')
    else:
        print('<'+word+'> is not acceptable.')