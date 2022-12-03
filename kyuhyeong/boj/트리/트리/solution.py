import sys

if __name__ == '__main__':
    nodes_cnt = int(sys.stdin.readline())
    tree = {n: {"parent": -1, "descendants": []} for n in range(nodes_cnt)}
    parents = list(map(int, sys.stdin.readline().split()))
    remove_node = int(sys.stdin.readline())

    for node, parent in enumerate(parents):
        if parent == -1:
            continue
        tree[node]["parent"] = parent

    # 각 노드에 대해 자신의 모든 후손 노드 검색
    for node in range(nodes_cnt):
        parent = tree[node]["parent"]
        while parent != -1:
            tree[parent]["descendants"].append(node)
            parent = tree[parent]["parent"]

    answer = 0
    for node in range(nodes_cnt):
        # remove_node의 모든 후손 노드들은 고려할 필요 없음
        if node in tree[remove_node]["descendants"] or node == remove_node:
            continue
        if node == tree[remove_node]["parent"] and len(tree[node]["descendants"]) == 1:
            answer += 1
        elif len(tree[node]["descendants"]) == 0:
            answer += 1

    print(answer)
