from collections import deque

def solution(n, wires):
    answer = n+1
    
    network = [[] for _ in range(n+1)]
    for x, y in wires:
        network[x].append(y)
        network[y].append(x)
    
    for x, y in wires:
        visited = [False] * (n+1)
        dq = deque([x])
        
        network[x].remove(y)
        network[y].remove(x)
        
        while dq:
            cur = dq.popleft()
            if visited[cur]:
                continue
            visited[cur] = True
            
            for node in network[cur]:
                if not visited[node]:
                    dq.append(node)
        
        network[x].append(y)
        network[y].append(x)
        
        num = visited.count(True)
        answer = min(answer, abs(n-num-num))
        
    return answer