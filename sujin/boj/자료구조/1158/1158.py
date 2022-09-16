if __name__ == '__main__':
    n, k = map(int, input().split(" "))
    queue = list(range(1, n+1)) # 1 2 3 4 5 6 7

    index = 0
    answer = []

    while len(queue) > 0:
        index += k-1
        index %= len(queue)
        answer.append(queue[index]) # k번째 사람 추가
        queue.pop(index) # k보다 앞에 있는 사람들 pop

    print("<{nums}>".format(nums=', '.join(map(str, answer))))


