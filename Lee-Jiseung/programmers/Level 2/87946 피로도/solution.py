from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    orders = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    for order in orders:
        curK = k
        temp = 0
        for i in order:
            if curK >= dungeons[i][0]:
                temp += 1
                curK -= dungeons[i][1]
        answer = max(answer, temp)
            
    return answer