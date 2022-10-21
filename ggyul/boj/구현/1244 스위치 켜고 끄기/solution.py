'''
https://www.acmicpc.net/problem/1244
1244 스위치 켜고 끄기

25M
1. 대칭 체크할때 for문에서 하고싶어서 for문에서 하다가 인덱스 에러나서 왠지 찾다가 그냥 투포인터 느낌으로 바꿨다.
2. 제대로 안보고 20개마다 줄바꿈 안해서 틀렸다
'''


n = int(input())
is_on = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    stud, switch = map(int, input().split())
    if stud == 1:
        for i in range(switch, n+1, switch):
            is_on[i-1] = 1 - is_on[i-1]
    else:
        is_on[switch-1] = 1 - is_on[switch-1]
        lo, hi = switch - 2, switch
        while 0 <= lo < hi < n:
            if is_on[lo] == is_on[hi]:
                is_on[lo] = 1 - is_on[lo]
                is_on[hi] = 1 - is_on[hi]
                lo -= 1
                hi += 1
            else:
                break

for i in range(0, len(is_on), 20):
    print(' '.join(map(str, is_on[i:i+20])))
