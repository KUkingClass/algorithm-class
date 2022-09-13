# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
import sys
input = sys.stdin.readline


n, k = map(int, input().strip().split())
is_out = [False for _ in range(n)]
pointer = 0
out_count = 0
ans = []
counter = 1  # 몇 번째인지
while out_count < n:
    # if pointer == n:
    #     pointer = 0
    pointer %= n
    if not is_out[pointer]:
        if counter == k:
            ans.append(pointer+1)  # zero based 인덱스라서 1-based로 변경
            is_out[pointer] = True
            out_count += 1
            counter = 1
        else:
            counter += 1
    pointer += 1
print('{}{}{}'.format('<', ', '.join(map(str, ans)), '>'))
