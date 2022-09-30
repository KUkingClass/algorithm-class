from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    d1 = deque(queue1)
    d2 = deque(queue2)
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    for i in range(n*4):
        if sum1 == sum2:
            return i
        elif sum1 < sum2:
            d1.append(d2[0])
            sum1 += d2[0]
            sum2 -= d2[0]
            d2.popleft()
        else:
            d2.append(d1[0])
            sum2 += d1[0]
            sum1 -= d1[0]
            d1.popleft()
    
    return -1
    