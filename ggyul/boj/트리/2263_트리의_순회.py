"""
https://www.acmicpc.net/problem/2263
트리의 순회

인오더   : 왼쪽 -> 루트 -> 오른쪽
포스트오더: 왼쪽 -> 오른쪽 -> 루트
-----------------------------
프리오더  : 루트 -> 왼쪽 -> 오른쪽

1. 포스트오더 맨 끝에서 루트를 찾는다
2. 인오더에서 해당 루트를 중심으로 왼쪽 / 오른쪽 을 찾는다
-> 이 개수만큼 포스트오더 에서 왼쪽 오른쪽도 찾을 수 있다
"""
import sys
sys.setrecursionlimit(100_005)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def go_preorder(in_from, in_to, post_from, post_to):
    root = postorder[post_to]
    print(root, end=' ')
    inorder_root_index = inorder.index(root)
    left_count = inorder_root_index - in_from
    right_count = in_to - inorder_root_index
    if left_count > 0:
        go_preorder(in_from, in_from + (left_count - 1), post_from, post_from + (left_count - 1))
    if right_count > 0:
        go_preorder(in_to - (right_count - 1), in_to, post_to - 1 - (right_count - 1), post_to - 1)


go_preorder(0, len(inorder) - 1, 0, len(postorder) - 1)
