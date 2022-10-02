import sys
from itertools import product
"""
   n = 500
   k = {8, 9} 라면
   답 : 99 (3자리수가 아닌 2자리수가 나올 수도 있다)
"""

_input = sys.stdin.readline

if __name__ == '__main__':
    (n, m) = map(int, _input().strip().split())
    k = sorted(set(map(int, _input().strip().split())), reverse=True)
    length = len(str(n))

    flag = True
    while flag:
        for pro in list(product(k, repeat=length)):
            now = int(''.join(map(str, pro)))

            if n >= now:
                print(now)
                flag = False
                break
        length -= 1
