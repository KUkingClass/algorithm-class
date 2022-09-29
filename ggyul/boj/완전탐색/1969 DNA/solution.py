'''
https://www.acmicpc.net/problem/1969
DNA
'''
import sys
_input = sys.stdin.readline
n, m = map(int, _input().split())
dna = [_input().strip() for _ in range(n)]

ans_dna = ''
ans_distance = 0

# 문자열 길이만큼 보면서
for i in range(m):
    dna_dict = {}
    # 각 dna의 문자가 몇 번 나왔는지 센다
    for j in range(n):
        if dna[j][i] in dna_dict:
            dna_dict[dna[j][i]] += 1
        else:
            dna_dict[dna[j][i]] = 1
    # 1. 정렬 시 길이가 크면 앞으로, 2. 길이가 같으면 문자열 작은 게 앞으로.
    # 그런데 전체 얻을 필요 없이 최소만 알면 되므로 정렬대신 min 사용
    max_item = min(dna_dict.items(), key = lambda x: (-x[1], x[0]))
    ans_dna += max_item[0]
    ans_distance += n - max_item[1]
print(ans_dna)
print(ans_distance)
