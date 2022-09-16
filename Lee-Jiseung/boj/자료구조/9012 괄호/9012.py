t = int(input())

for _ in range(t):
    str = input()
    flag = "YES"
    count = 0
    
    for c in str:
        if c == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                flag = "NO"
                break
                
    if count != 0:
        flag = "NO"
    print(flag)