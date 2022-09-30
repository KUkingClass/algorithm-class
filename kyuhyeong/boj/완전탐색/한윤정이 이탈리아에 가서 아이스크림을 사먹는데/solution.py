import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    combinations = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    no_list = {i_num: set() for i_num in range(1, n + 1)}
    
    for combination in combinations:
        key, val = sorted(combination)
        no_list[key].add(val)

    answer = 0

    for d1 in range(1, n - 1):
        stack = [d1]
        for d2 in range(d1 + 1, n):
            if d2 not in no_list[stack[-1]]:
                stack.append(d2)
                for d3 in range(d2 + 1, n + 1):
                    possible = True
                    for key in stack:
                        if d3 in no_list[key]:
                            possible = False
                            break
                    if possible:
                        answer += 1
                stack.pop()

    print(answer)
        