import sys

nodes = []
while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except ValueError as e:
        break

def divide(nums):
    start, end = nums
    root = nodes[start]
    left = [start+1, start+1]
    right = [end, end]
    for i in range(start+1, end):
        if nodes[i] > root:
            right[0] = i
            break
        left[1] += 1
    return root, left, right

stack = [[0, len(nodes)]]
answer = []
while stack:
    root, left_subtree, right_subtree = divide(stack.pop())
    answer.append(root)
    if left_subtree[1] - left_subtree[0] > 0:
        stack.append(left_subtree)
    if right_subtree[1] - right_subtree[0] > 0:
        stack.append(right_subtree)

answer.reverse()
print(*answer, sep='\n')