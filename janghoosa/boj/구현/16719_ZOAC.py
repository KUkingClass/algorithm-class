# 16719 ZOAC
# https://www.acmicpc.net/problem/16719
a1 = input()
res = ["" for _ in range(len(a1))]

def printDict(a1, b1):
    if not b1:
        return
    minb1 = min(b1)
    tmp = b1.index(minb1)
    res[a1+tmp] = minb1
    print("".join(res))
    printDict(a1+tmp+1, b1[tmp+1:])
    printDict(a1, b1[:tmp])

printDict(0, a1)