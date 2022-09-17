def func(x):
    count1 = 0
    count2 = 0
    temp = ""
    answer = 0
        
    for s in x:
        temp += s
        
        if s == '(':
            count1 += 1
        elif s == ')':
            count1 -= 1
            if count1 < 0:
                return 0
        elif s == '[':
            count2 += 1
        elif s == ']':
            count2 -= 1
            if count2 < 0:
                return 0

        if count1 == 0 and count2 == 0:
            if temp == "()":
                answer += 2
            elif temp == "[]":
                answer += 3
            elif temp[0] == '(':
                answer += 2*func(temp[1:-1])
            else:
                answer += 3*func(temp[1:-1])
            temp = ""

    if count1 != 0 or count2 != 0:
        return 0
            
    return answer


x = input()
print(func(x))