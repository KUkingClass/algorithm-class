def solution(numbers):
    answer = []
    
    for number in numbers:
        if number & 1 == 0:
            answer.append(number+1)
            continue
        
        n = 1
        while True:
            if (number & (1 << n) == 0) and (number & (1 << (n-1))):
                answer.append(number + (1<<(n-1)))
                break
            n += 1
    return answer