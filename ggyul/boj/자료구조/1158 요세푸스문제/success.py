# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
pointer = 0
out_count = 0
ans = []
while len(nums) > 0:
    pointer += k-1
    pointer %= len(nums)
    ans.append(nums[pointer])
    nums.pop(pointer)
print('{}{}{}'.format('<', ', '.join(map(str, ans)), '>'))
