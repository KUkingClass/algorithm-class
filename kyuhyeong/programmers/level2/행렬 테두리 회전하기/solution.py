from collections import deque

def solution(rows, columns, queries):
    matrix = [[columns*j + i for i in range(1, columns + 1)] for j in range(rows)]

    queue = deque()
    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        for j in range(y1, y2 + 1):
            queue.append(matrix[x1][j])
        for i in range(x1 + 1, x2 + 1):
            queue.append(matrix[i][y2])
        for j in range(y2 - 1, y1 - 1, -1):
            queue.append(matrix[x2][j])
        for i in range(x2 - 1, x1, -1):
            queue.append(matrix[i][y1])

        queue.rotate()
        answer.append(min(queue))
        for j in range(y1, y2 + 1):
            matrix[x1][j] = queue.popleft()
        for i in range(x1 + 1, x2 + 1):
            matrix[i][y2] = queue.popleft()
        for j in range(y2 - 1, y1 - 1, -1):
            matrix[x2][j] = queue.popleft()
        for i in range(x2 - 1, x1, -1):
            matrix[i][y1] = queue.popleft()

    return answer



if __name__ == '__main__':
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(solution(rows, columns, queries))
