import sys

# N장의 카드 1..N, 1이 제일 위
# 제일 위에 있는 카드 바닥에 버리고
# 그 다음 제일 위에 카드를
# 제일 아래 있는 카드 밑에 둠
# 카드 한개 남을 때까지 반복

if __name__ == '__main__':
    _input = sys.stdin.readline
    n = int(_input())

    card = []

    for i in range(n):
        card.append(i + 1)

    pointer = 0
    while True:
        curSize = len(card) - pointer

        if curSize == 1:
            break

        # 맨 위에 버린다
        pointer += 1

        # 맨 위에것 뒤에 붙인다
        card.append(card[pointer])
        pointer += 1

    print(card[pointer])
