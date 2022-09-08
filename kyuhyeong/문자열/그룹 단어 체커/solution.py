import sys


if __name__ == '__main__':
    test_case_size = int(input())
    test_cases = [sys.stdin.readline().strip() for _ in range(test_case_size)]
    answer = 0

    for case in test_cases:
        words = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
        if len(case) == 1:
            answer += 1
            continue
        prev = case[0]
        words[prev] += 1
        is_group = True
        for cur in case[1:]:
            if words[cur] > 0 and prev != cur:
                is_group = False
                break
            words[cur] += 1
            prev = cur
        if is_group:
            answer += 1

    print(answer)
