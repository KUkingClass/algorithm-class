import re
import sys
from functools import cmp_to_key

pattern = re.compile("[a-zA-Z]|[0-9]+")


def compare(x, y):
    len_x = len(x)
    len_y = len(y)

    x = re.findall(pattern, x)
    y = re.findall(pattern, y)

    for x1, y1 in zip(x, y):
        if x1 == y1:
            continue

        if x1.isdigit():
            if y1.isdigit():
                difference = int(x1) - int(y1)
                if difference != 0:
                    return difference
                return x1.count("0") - y1.count("0")
            return -1
        elif y1.isdigit():
            return 1
        else:
            if x1.lower() == y1.lower():
                return ord(x1) - ord(y1)
            return ord(x1.lower()) - ord(y1.lower())

    return len_x - len_y


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    files = [sys.stdin.readline().strip() for _ in range(N)]

    files.sort(key=cmp_to_key(compare))

    for file in files:
        print(file)
