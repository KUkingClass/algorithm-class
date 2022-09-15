import sys


def parenthesis_check(case):
    count = 0
    for parenthesis in case:
        if parenthesis == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return False if count else True


if __name__ == '__main__':
    case_size = int(sys.stdin.readline())
    for _ in range(case_size):
        case = sys.stdin.readline().strip()
        if parenthesis_check(case):
            print("YES")
        else:
            print("NO")
