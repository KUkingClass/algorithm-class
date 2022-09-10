# https://www.acmicpc.net/problem/16916
import re

s, p = input(), input()
if s.find(p) != -1:
    print(1)
else:
    print(0)