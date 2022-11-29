'''
https://www.acmicpc.net/problem/5639
이진 검색 트리

pypy로하면 메모리 초과나고 python으로 해야 통과
'''
import sys

sys.setrecursionlimit(10_005)

values = []
while True:
    try:
        values.append(int(sys.stdin.readline()))
    except:
        break


def post_order_search(lo, hi):
    # mid값 초기화 시 hi + 1으로 초기화했으므로, 끝까지 다 보면 lo가 hi보다 커진다
    if lo > hi:
        return
    # 왼쪽 서브트리를 찾기 위해 나보다 커지는 지점을 찾는다.
    mid = hi + 1
    for i in range(lo + 1, hi + 1):
        if values[i] > values[lo]:
            mid = i
            break
    post_order_search(lo + 1, mid - 1)
    post_order_search(mid, hi)
    print(values[lo])


# 후위 순회
post_order_search(0, len(values) - 1)
