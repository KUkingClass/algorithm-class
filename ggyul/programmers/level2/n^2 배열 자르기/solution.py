'''
https://school.programmers.co.kr/learn/courses/30/lessons/87390
n^2 배열 자르기

진짜 n^2에 대해서 다 돌면 10^14로 시간초과
right - left 는 10^5이므로 이 사이를 도는 건 시간초과 나지 않는다.
따라서 left ~ right까지 인덱스를 기반으로 해당 인덱스에 어떤 값이 있을 지 알면 된다.
'''


def solution(n, left, right):
    answer = []

    def get_num(index):
        row, col = divmod(index, n)
        if col <= row:
            return row+1  # 배열 안에 값은 1 기반 인덱스임에 주의 !!
        return col+1  # 배열 안에 값은 1 기반 인덱스임에 주의 !!

    for i in range(left, right+1):
        answer.append(get_num(i))

    return answer
