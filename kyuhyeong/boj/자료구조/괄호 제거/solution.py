import sys
from itertools import combinations

if __name__ == '__main__':
    expression = sys.stdin.readline().strip()
    count = expression.count("(")

    open_parentheses = []
    parenthesis_num = 0

    parentheses = [[] for _ in range(count)]

    for i, ch in enumerate(expression):
        if ch == "(":
            open_parentheses.append(parenthesis_num)
            parentheses[parenthesis_num].append(i)
            parenthesis_num += 1
        elif ch == ")":
            parentheses[open_parentheses[-1]].append(i)
            open_parentheses.pop()

    answer = []

    for r in range(1, count + 1):
        for combination in combinations(range(count), r):
            exp = list(expression)

            for idx in combination:
                open_idx, close_idx = parentheses[idx]
                exp[open_idx] = exp[close_idx] = ""

            answer.append("".join(exp))

    for line in sorted(set(answer)):
        print(line)
