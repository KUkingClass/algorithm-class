'''
https://www.acmicpc.net/problem/5639
이진 검색 트리
1H?

이진 트리에서 삽입하는 방법은 해당하는 번호의 노드를 탐색해보고, 실패했을 때가 그 자리
이를 이용해서 삽입하면서 트리를 만든다.
---
찾아보니 진짜 나처럼 트리를 만드는 게 아니고..
전위면 루트 -> 왼쪽 -> 오른쪽이고
후위면 오른쪽 -> 왼쪽 -> 루트니까
첫 값은 중간값
그럼 첫 값보다 작은 건 왼쪽 서브트리,
첫 값보다 큰 건 오른쪽 서브트리로 나눠서 후위순회를 돌리는 것 같다.
'''
import sys

sys.setrecursionlimit(10_005)

tree = [[]]
root = int(input())
tree.append([root, 0, 0])

values = []
while True:
    try:
        values.append(int(sys.stdin.readline()))
    except:
        break

for new_value in values:
    target = 1
    while target != 0:
        if tree[target][0] < new_value:
            if tree[target][2] == 0:
                tree.append([new_value, 0, 0])
                tree[target][2] = len(tree)-1
                break
            target = tree[target][2]
        else:
            if tree[target][1] == 0:
                tree.append([new_value, 0, 0])
                tree[target][1] = len(tree)-1
                break
            target = tree[target][1]


def post_order_search(node):
    if node == 0:
        return
    post_order_search(tree[node][1])
    post_order_search(tree[node][2])
    print(tree[node][0])


# 후위 순회
post_order_search(1)
