'''
https://www.acmicpc.net/problem/2422
한윤정이 이탈리아에 가서 아이스크림을 사먹는데
'''
n, m = map(int, input().split())
is_bad = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    ice1, ice2 = map(int, input().split())
    is_bad[ice1][ice2] = True
    is_bad[ice2][ice1] = True

ans = 0


def search(start, added):
    if len(added) == 3:
        global ans
        ans += 1
        return
    if start > n:
        return
    if len(added) == 0 or not any(is_bad[start][ice] for ice in added):
        added.append(start)
        search(start+1, added)
        added.pop()
    search(start+1, added)


search(1, [])
print(ans)