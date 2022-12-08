"""
숫자보다 1 큰 수부터 시작해서 2개 이하 다를 때까지 찾으면 시간 초과가 발생한다.
숫자 범위가 10^15라서 하나씩 찾으면 시간 초과가 나는 듯하다.

따라서 규칙을 이용한다.

값을 살펴보면
00001111이면
00010111,
00010010011이면
00010010101으로
01 -> 10으로 바꾸는 게 무조건 가장 작음
단 끝이 0일 경우 그냥 1을 더하는 게 낫다

1. 맨 끝이 0이면 1만 더한다
2. 그게 아니면 가장 작은 쪽에서 01을 찾고 10으로 바꾼다
"""

def count_bit(number):
    print(format(number, 'b'))
    bit = []
    while number:
        bit.append(number % 2)
        number //= 2
    print(bit)
    return bit


def solution(numbers):
    answer = []
    for number in numbers:
        binary = format(number, 'b')
        if binary[-1] == '0':
            answer.append(number+1)
        else:
            binary = '0' + binary
            for i in range(len(binary)-2, -1, -1):
                if binary[i:i+2] == '01':
                    answer_binary = binary[:i] + '10' + binary[i+2:]
                    answer.append(int(answer_binary, 2))
                    break
    return answer
