from collections import deque


def solution(s):
    sequence = deque(s)
    answer = 0
    for _ in range(len(s)):
        if is_right(sequence):
            answer += 1
        sequence.rotate(-1)

    return answer


def is_right(sequence):
    stack = []
    pair = {"}": "{", "]": "[", ")": "("}
    for sub in sequence:
        if sub in ["{", "(", "["]:
            stack.append(sub)
        elif stack and stack[-1] == pair[sub]:
            stack.pop()
        else:
            return False

    return not stack


if __name__ == '__main__':
    s = "}]()[{"
    print(solution(s))
