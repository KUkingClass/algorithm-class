n = int(input())

heights = list(map(int, input().split()))
answer = [0 for _ in range(n)]

stack = []
for i, height in enumerate(heights):
    while len(stack) > 0:
        if stack[-1][1] <= height:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
        
    stack.append([i, height])
        
    
for a in answer:
    print(a, end=' ')