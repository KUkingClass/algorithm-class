def solution(rows, columns, queries):
    answer = []
    matrix = [[j*columns + i+1 for i in range(columns)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:
        left_top = matrix[x1-1][y1-1]
        min_num = left_top
        for x in range(x1-1, x2-1):
            min_num = min(min_num, matrix[x+1][y1-1])
            matrix[x][y1-1] = matrix[x+1][y1-1]
        for y in range(y1-1, y2-1):
            min_num = min(min_num, matrix[x2-1][y+1])
            matrix[x2-1][y] = matrix[x2-1][y+1]
        for x in range(x2-1, x1-1, -1):
            min_num = min(min_num, matrix[x-1][y2-1])
            matrix[x][y2-1] = matrix[x-1][y2-1]
        for y in range(y2-1, y1-1, -1):
            min_num = min(min_num, matrix[x1-1][y-1])
            matrix[x1-1][y] = matrix[x1-1][y-1]
        matrix[x1-1][y1] = left_top
        answer.append(min_num)
        
    return answer
