import re
import sys


# == 틀림!! 0012와 12 비교 안되는 문제 발생 == #
def natural_sort(file):
    return [int(f) if f.isdigit() and f[0] != '0' else f for f in re.split("([0-9]+)", file)]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    files = [sys.stdin.readline().strip() for _ in range(N)]

    files.sort(key=natural_sort)

    for file in files:
        print(file)

# 3
# Foo9Bar
# Foo00012Bar
# 12000Foo1Bar
