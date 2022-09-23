# https://school.programmers.co.kr/learn/courses/30/lessons/92335
import math
def tenton(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**(1/2))+1):
        if x % i != 0:
            pass
        else:
            return False
    return True

def solution(n, k):
    answer = 0
    A = tenton(n,k).split('0')
    for i in A:
        if i != '' and is_prime(int(i)):
                answer += 1
    return answer