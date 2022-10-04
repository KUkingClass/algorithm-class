'''
https://www.acmicpc.net/problem/18511
큰 수 구성하기

처음에 무조건 k 자릿수로만 구해서 틀리고
k보다 작을 때로 고쳤는데
k보다 클 때를 빼먹어서 틀렸다 ^..^
'''

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)


def find_answer(count, max_count, result):
    if count == max_count:
        if result <= n:
            print(result)
            return True
        else:
            return False
    for num in nums:
        # 정답을 찾으면 더 안들어가고 return
        if find_answer(count+1, max_count, result*10+num):
            return True

    return 0


n_count = len(str(n))

for i in range(n_count, 0, -1):
    if find_answer(0, i, 0):
        break
