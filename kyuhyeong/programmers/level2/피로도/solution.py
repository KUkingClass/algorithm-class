from itertools import permutations


def solution(k, dungeons):
    num_dungeons = len(dungeons)
    answer = 0

    for permutation in permutations(range(num_dungeons), num_dungeons):
        answer = max(answer, play(k, dungeons, permutation))

    return answer


def play(k, dungeons, permutation):
    count = 0
    for order in permutation:
        required, consume = dungeons[order]
        if k < required:
            break
        k -= consume
        count += 1

    return count


if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))
