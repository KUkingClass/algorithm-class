import sys

if __name__ == '__main__':
    num_switches = int(sys.stdin.readline())
    switches = [-1]
    switches.extend(map(int, sys.stdin.readline().split()))
    num_students = int(sys.stdin.readline())

    for _ in range(num_students):
        gender, num = map(int, sys.stdin.readline().split())
        if gender == 1:
            for i in range(num, num_switches + 1, num):
                switches[i] = (switches[i] + 1) % 2
        else:
            stride = 0
            for s in range(1, min(num, num_switches - num + 1)):
                if switches[num + s] != switches[num - s]:
                    break
                stride = s
            for i in range(num - stride, num + stride + 1):
                switches[i] = (switches[i] + 1) % 2

    for i in range(1, num_switches + 1):
        print(switches[i], end=' ')
        if i % 20 == 0:
            print()
