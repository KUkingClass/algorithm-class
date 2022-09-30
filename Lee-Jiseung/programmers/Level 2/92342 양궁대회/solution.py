def func(ryans, n):
    if ryans[0] == n:
        return False
    
    for i in range(11):
        if ryans[i] > 0:
            if i == 0:
                r = ryans[0]
                ryans[0] = 0
                for j in range(1, 11):
                    if ryans[j] > 0:
                        ryans[j] -= 1
                        ryans[j-1] += r + 1
                        break
            else:
                ryans[i] -= 1
                ryans[i-1] += 1
            return True    

        
def solution(n, info):
    answer = [-1]
    ryans = [ 0 for _ in range(10) ]
    ryans.append(n)
    diff = 0
    
    while True:
        score_apeach = 0
        score_ryan = 0
        for i in range(10):
            if ryans[i] < info[i]:
                score_apeach += 10 - i
            elif ryans[i] == info[i] and ryans[i] > 0:
                score_apeach += 10 - i
            elif ryans[i] > info[i]:
                score_ryan += 10 - i
        
        if score_ryan > score_apeach:
            if score_ryan- score_apeach > diff:
                answer = ryans.copy()
                diff = score_ryan- score_apeach
        if func(ryans, n) == False:
            break
            
    return answer