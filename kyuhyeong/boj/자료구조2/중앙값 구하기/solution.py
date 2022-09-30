import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        m = int(sys.stdin.readline())
        sequence = []
        while len(sequence) != m:
            sequence.extend(list(map(int, sys.stdin.readline().split())))

        answer = []
        for i in range(0, m, 2):
            answer.append(sorted(sequence[:i + 1])[i // 2])

        length_answer = len(answer)
        print(length_answer)
        start = 0
        end = min(10, length_answer)

        while start < end:
            print(" ".join(map(str, answer[start: end])))
            start = end
            end = min(end + 10, length_answer)
