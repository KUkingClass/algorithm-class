import sys


def check(circles):
    circles.sort(key=lambda circle: circle[0])

    stack = []
    coordinate = {}

    for point, circle_num, status in circles:
        if point in coordinate:
            return False

        if status == "open":
            stack.append(circle_num)
        else:
            if stack[-1] != circle_num:
                return False
            stack.pop()
        coordinate[point] = True

    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    circles = []

    for i in range(n):
        x, r = map(int, sys.stdin.readline().split())
        circles.append((x - r, i, "open"))
        circles.append((x + r, i, "close"))

    if check(circles):
        print("YES")
    else:
        print("NO")
