'''
https://school.programmers.co.kr/learn/courses/30/lessons/87946
피로도

던전을 최대한 많이 탐험
최대 던전 수 리턴
던전 길이 8이므로 완전 탐색하면 됨
'''
import itertools


def solution(k, dungeons):
    answer = -1
    n = len(dungeons)

    arr = [i for i in range(n)]
    perms = itertools.permutations(arr, n)

    def explore(perm):
        fatigue = k
        explored = 0
        for dungeon in perm:
            if fatigue < dungeons[dungeon][0]:
                break
            fatigue -= dungeons[dungeon][1]
            explored += 1
        return explored

    for perm in perms:
        answer = max(answer, explore(perm))
    return answer
