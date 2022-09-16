import sys
from math import inf

if __name__ == '__main__':
    test_size = int(sys.stdin.readline())

    for _ in range(test_size):
        case = sys.stdin.readline().strip()
        target_size = int(sys.stdin.readline())

        alphabet = {chr(ch): {
            "indices": [],
            "occurrence": 0
        } for ch in range(ord('a'), ord('z') + 1)}

        for i, char in enumerate(case):
            alphabet[char]["occurrence"] += 1
            alphabet[char]["indices"].append(i)

        min_length = inf
        max_length = -inf

        for val in alphabet.values():
            if val["occurrence"] < target_size:
                continue
            for i in range(val["occurrence"] - target_size + 1):
                distance = val["indices"][i + target_size - 1] - val["indices"][i] + 1
                min_length = min(min_length, distance)
                max_length = max(max_length, distance)

        if min_length == inf or max_length == -inf:
            print(-1)
        else:
            print(min_length, max_length)
