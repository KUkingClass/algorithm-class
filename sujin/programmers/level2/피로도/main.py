from itertools import permutations

"""
  최소 필요 피로도 -> 던전을 탐험하기 위한 최소한의 피로도
  소모 피로 -> 던전 마친 후 소모되는 피로도
  유저가 탐험할 수 있는 최대 던전 수?
"""


def solution(k, dungeons):
    answer = -1
    num_dungeon = len(dungeons)
    perms = permutations(dungeons, num_dungeon)

    for perm in perms:
        answer = max(answer, explore(k, perm))

    return answer


# 던전 리스트 탐험
def explore(k, perm):
    cnt = 0
    cur_pirodo = k

    for dun in perm:
        min_pirodo, need_pirodo = dun[0], dun[1]
        if cur_pirodo < min_pirodo: # 입장 못함
            break

        cur_pirodo -= need_pirodo
        cnt += 1
    return cnt


if __name__ == '__main__':
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    print(solution(k, dungeons))



