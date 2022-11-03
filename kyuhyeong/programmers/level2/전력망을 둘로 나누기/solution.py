from collections import deque


def solution(n, wires):
    graph = {i: [] for i in range(1, n + 1)}
    min_difference = n + 1

    for node1, node2 in wires:
        graph[node1].append([node2, True])
        graph[node2].append([node1, True])

    for node, neighbors in graph.items():
        for idx, neighbor in enumerate(neighbors):
            graph[node][idx][1] = False
            group = bfs(graph, node, n)
            min_difference = min(min_difference, abs(n - 2*group))
            graph[node][idx][1] = True

    return min_difference


def bfs(graph, start, n):
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    group = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor, connected in graph[node]:
            if not connected:
                continue
            if not visit[neighbor]:
                visit[neighbor] = True
                queue.append(neighbor)
                group += 1

    return group


if __name__ == '__main__':
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires))
