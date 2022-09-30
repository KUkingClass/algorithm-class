def isPrime(num):
    if num < 2:
        return False
    i=2
    while i*i<=num:
        if num % i == 0:
            return False
        i+=1
    return True

    
def solution(n, k):
    answer = 0
    
    num = 0
    notBiggerThanN = 1
    while notBiggerThanN < n:
        notBiggerThanN *= k
    if notBiggerThanN > n:
        notBiggerThanN //= k
        
    while notBiggerThanN > 0:
        
        temp = n//notBiggerThanN
        n -= temp * notBiggerThanN
        notBiggerThanN //= k
        
        if temp == 0:
            if isPrime(num):
                answer+=1
            num = 0
        else:
            num = num*10 + temp
    if isPrime(num):
        answer+=1
    return answer