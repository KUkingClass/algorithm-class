from functools import cmp_to_key

n = int(input())
arr = []
for i in range(n):
    arr.append(input())


def num_to_list(word):
    li = list(word)
    i = 0
    while i < len(li):
        if li[i].isdigit():
            num = i
            while num < len(li) and li[num].isdigit():
                num += 1
            li[i:num] = [''.join(li[i:num])]
            i = num - 1
        i += 1
    return li


def compare(x, y):
    x = num_to_list(x)
    y = num_to_list(y)
    i = 0

    while i < min(len(x), len(y)):
        if x[i] == y[i]:
            i += 1
            continue
        elif x[i].isdigit() and y[i].isdigit():
            xi = int(x[i])
            yi = int(y[i])
            if xi == yi:
                xz = len(x[i]) - len(x[i].lstrip('0'))
                yz = len(y[i]) - len(y[i].lstrip('0'))
                return -1 if xz < yz else 1
            return -1 if xi < yi else 1
        elif x[i].isalpha() and y[i].isalpha():
            xl = x[i].lower()
            yl = y[i].lower()
            if xl == yl:
                return -1 if x[i] < y[i] else 1
            return -1 if xl < yl else 1
        elif x[i].isalpha() and y[i].isdigit():
            return 1
        elif x[i].isdigit() and y[i].isalpha():
            return -1
        i += 1
    return -1 if len(x) < len(y) else 1


arr.sort(key=cmp_to_key(compare))

for i in arr:
    print(i)
