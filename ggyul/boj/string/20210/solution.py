# https://www.acmicpc.net/problem/20210
from functools import cmp_to_key

n = int(input())
arr = []
for i in range(n):
    arr.append(input())


def get_digit_from_index(word, index):
    count = 0
    for i in range(index, len(word)):
        if word[i].isdigit():
            count += 1
        else:
            break
    return word[index:index + count]


def compare(x, y):
    l, r = 0, 0
    # while이 아닌 for문일 경우 카운터 변수 수정 불가능
    while l < len(x):
        if r >= len(y):
            return 1
        # 둘다 문자
        if x[l].isalpha() and y[r].isalpha():
            # 같은 문자일 경우 --> 무조건 대문자, 소문자로 비교해서 틀렸었다..
            if x[l].upper() == y[r].upper():
                # 대문자가 앞
                if x[l].isupper() and y[r].islower():  # 그대로
                    return -1
                if x[l].islower() and y[r].isupper():
                    return 1
            # 다른 문장일 경우
            elif x[l].upper() < y[r].upper():
                return -1
            else:
                return 1
            l += 1
            r += 1
        # 둘다 숫자
        elif x[l].isdigit() and y[r].isdigit():
            # 숫자 끝까지 추출
            x_digit = get_digit_from_index(x, l)
            y_digit = get_digit_from_index(y, r)
            if int(x_digit) == int(y_digit):
                if len(x_digit) < len(y_digit):
                    return -1
                elif len(x_digit) > len(y_digit):
                    return 1
            elif int(x_digit) > int(y_digit):
                return 1
            elif int(x_digit) < int(y_digit):
                return -1
            l += len(x_digit)
            r += len(y_digit)
        # 한 쪽만 문자
        elif x[l].isalpha() and y[r].isdigit():
            return 1
        elif x[l].isdigit() and y[r].isalpha():
            return -1
    if r < len(y):
        return -1
    return 0


arr.sort(key=cmp_to_key(compare))

for a in arr:
    print(a)
