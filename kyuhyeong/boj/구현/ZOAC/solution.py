import sys


def show(sequence, subsequence, direction, last_idx):
    if not sequence:
        return subsequence
    pivot = min(sequence)

    if direction == "right":
        subsequence.insert(last_idx + 1, pivot)
        last_idx += 1
    else:
        subsequence.insert(last_idx, pivot)
    print("".join(subsequence))

    pivot_idx = sequence.find(pivot)

    show(sequence[pivot_idx + 1:], subsequence, "right", last_idx)
    show(sequence[:pivot_idx], subsequence, "left", last_idx)


if __name__ == '__main__':
    sequence = sys.stdin.readline().strip()
    show(sequence, [], "right", -1)
