import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    words = list(set(sys.stdin.readline().strip() for _ in range(N)))
    words.sort(key=lambda word: (len(word), str(word)))

    for word in words:
        print(word)
