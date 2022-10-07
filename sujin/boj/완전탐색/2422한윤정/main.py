import sys
from itertools import combinations
"""
   n개 아이스크림, m가지 섞으면 안되는 조합
   1 -> 2, 3
   2 -> 1
   3 -> 1, 4
   4 -> 1
"""

_input = sys.stdin.readline

if __name__ == '__main__':
    (n, m) = map(int, _input().strip().split())
    ice_cream = [i+1 for i in range(n)]
    no_mix = {i: set() for i in range(1, n+1)}
    answer = 0

    # 섞으면 안되는 조합 딕셔너리 생성
    for _ in range(m):
        (n1, n2) = map(int, input().strip().split())
        no_mix[n1].add(n2)
        no_mix[n2].add(n1)

    # 미리 3가지 뽑아서 순회
    # 3가지 조합 중, no_mix에 모두 위배되지 않으면 OK
    for comb in list(set(combinations(ice_cream, 3))):
        (n1, n2, n3) = comb
        if n1 not in no_mix[n2] and n1 not in no_mix[n3] and n2 not in no_mix[n3]:
            answer += 1

    print(answer)




