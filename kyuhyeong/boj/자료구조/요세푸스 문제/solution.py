import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    people = [i for i in range(1, n + 1)]

    i = 0
    answer = []
    length = n
    while length:
        i = (k - 1) % length
        length -= 1
        answer.append(str(people[i]))
        people = people[i+1:] + people[:i]

    print("<{}>" .format(", ".join(answer)))
