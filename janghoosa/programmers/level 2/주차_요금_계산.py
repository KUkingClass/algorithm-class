# 92341 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

def calculate_time(time1, time2):
    t2 = list(map(int,time2.split(':')))
    t1 = list(map(int,time1.split(':')))
    hour = t2[0]-t1[0]
    if t2[1] > t1[1]:
        mi = t2[1]-t1[1]
    else:
        mi = 60 - t1[1] + t2[1]
        hour -= 1
    return hour*60 + mi

def solution(fees, records):
    answer = []
    A = {}
    B = {}
    for i in records:
        arr = i.split()
        if arr[2] == 'IN':
            B[arr[1]]=arr[0]
        else:
            if arr[1] in B:
                if arr[1] not in A:
                    A[arr[1]] = 0
                A[arr[1]] += calculate_time(B[arr[1]], arr[0])
                del B[arr[1]]
    if B:
        for i in B:
            if i not in A:
                A[i] = 0
            A[i] += calculate_time(B[i], '23:59')
    C = sorted(A.items())
    for i in C:
        time = i[1]
        if time > fees[0]:
            time -= fees[0]
            time /= fees[2]
            time = math.ceil(time)
            ans = time*fees[3] + fees[1]
        else:
            ans = fees[1]
        answer.append(ans)
    return answer