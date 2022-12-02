import sys
sys.setrecursionlimit(10**6)


def solution(n, inorder, postorder):
    node_indices = [0 for _ in range(n + 1)]    # inorder 노드의 인덱스 저장
    for i in range(n):
        node_indices[inorder[i]] = i

    def preorder(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return
        sub_root = postorder[post_end]
        print(sub_root, end=' ')

        preorder(in_start, node_indices[sub_root] - 1, post_start, post_start + node_indices[sub_root] - in_start - 1)
        preorder(node_indices[sub_root] + 1, in_end, post_end - in_end + node_indices[sub_root], post_end - 1)

    preorder(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder = list(map(int, sys.stdin.readline().split()))
    solution(n, inorder, postorder)
