d = {0:'', 1:'A', 2:'E', 3:'I', 4:'O', 5:'U'}

def num2alpha(x):
    return d[x]

def solution(word):
    answer = 0
    cur = [0] * 5
    
    while word != ''.join(list(map(lambda x: num2alpha(x),cur))):
        answer += 1
        flag = False
        for i in range(5):
            if cur[i] == 0:
                cur[i] += 1
                flag = True
                break
        if flag:
            continue
        cur[4] += 1
        for i in range(4, -1, -1):
            if cur[i] > 5:
                cur[i] = 0
                cur[i-1] += 1
        
    return answer