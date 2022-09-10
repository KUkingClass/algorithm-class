import sys

if __name__ == '__main__':
    source = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()

    if source.find(target) != -1:
        print(1)
    else:
        print(0)
