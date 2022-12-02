import sys

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder = []
stack = [[0, len(inorder), 0, len(postorder)]]
while stack:
    start_inorder, end_inorder, start_postorder, end_postorder = stack.pop()
    preorder.append(postorder[end_postorder-1])

    for i in range(start_inorder, end_inorder):
        if inorder[i] == postorder[end_postorder-1]:
            if i < end_inorder-1:
                stack.append([i+1, end_inorder, end_postorder-1 - (end_inorder-i-1), end_postorder-1])
            if start_inorder < i:
                stack.append([start_inorder, i, start_postorder, start_postorder + i-start_inorder])
            break

print(*preorder)
