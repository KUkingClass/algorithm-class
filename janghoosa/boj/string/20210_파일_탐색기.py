# 20210 파일 탐색기
# https://www.acmicpc.net/problem/20210
from functools import cmp_to_key
import sys
input = sys.stdin.readline
N = int(input())
A = [input().strip() for _ in range(N)]

def to_list(word):
    arr = list(word)
    i = 0
    while i < len(arr):
        if arr[i].isdigit():
            end = i
            while end < len(arr) and arr[end].isdigit():
                end += 1
            arr[i:end] = [''.join(arr[i:end])]
            i = end -1
        i += 1
    return arr

def diff(w1, w2):
    w1 = to_list(w1)
    w2 = to_list(w2)
    i = 0
    while i < min(len(w1), len(w2)):
        fir = w1[i]
        sec = w2[i]
        if fir == sec:
            i +=1
            continue
        if fir.isdigit() and sec.isalpha():
            return -1
        elif fir.isalpha() and sec.isdigit():
            return 1
        elif fir.isalpha() and sec.isalpha():
            if fir.lower() == sec.lower():
                if fir < sec:
                    return -1
                else:
                    return 1
            if fir.lower() < sec.lower():
                return -1
            else:
                return 1
        elif fir.isdigit() and sec.isdigit():
            if int(fir) == int(sec):
                zero1 = len(fir) - len(fir.lstrip('0'))
                zero2 = len(sec) - len(sec.lstrip('0'))
                if zero1 < zero2:
                    return -1
                else:
                    return 1
            else:
                if int(fir) < int(sec):
                    return -1
                else:
                    return 1
        i += 1
    if len(w1) < len(w2):
        return -1
    else:
        return 1

A.sort(key=cmp_to_key(diff))
for i in A:
    print(i)