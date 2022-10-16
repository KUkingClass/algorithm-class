'''
https://www.acmicpc.net/problem/14719
빗물
'''

h, w = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0

# 어차피 맨 아래는 블럭이 다 차있고, 비가 오면 그 위로도 계속 차므로 바닥은 신경쓸 필요가 없다.
for i in range(1, h+1):  # 아래부터, 0은 다 채워져있음
    is_in = False
    cnt = 0
    for j in range(w):
        if heights[j] >= i:  # 현재 블럭임
            if is_in and cnt > 0:
                ans += cnt
                cnt = 0
            else:
                is_in = True
        elif is_in:
            cnt += 1


print(ans)
