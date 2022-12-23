"""
https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=python3

1 base index
바뀐 숫자 중 가장 작은 숫자를 순서대로

계속 테케만 통과하고 제출해서 안됐었는데;;
board에서 내용 채울 때 i * columns를 해야되는데 계속 i * rows를 해서 틀렸다..
근데 테케는 거의 정방행렬만 주어져서 예제에서 이유를 찾지 못했다.
배열 주어졌을 때 정방행렬 아닌 것도 테케 넣어보기..
"""


def solution(rows, columns, queries):
    answer = []

    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for query in queries:
        from_x, from_y, to_x, to_y = (q - 1 for q in query)

        corners = [
            [from_x, to_y],
            [to_x, to_y],
            [to_x, from_y],
            [from_x, from_y],
        ]

        cache = board[from_x][from_y]
        min_value = cache

        cur_x, cur_y = from_x, from_y
        for i in range(4):
            while [cur_x, cur_y] != corners[i]:
                cur_x += dx[i]
                cur_y += dy[i]
                cache, board[cur_x][cur_y] = board[cur_x][cur_y], cache
                min_value = min(min_value, cache)
        answer.append(min_value)
    return answer
