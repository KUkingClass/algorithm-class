"""
https://www.acmicpc.net/problem/16987
* 문제
계란 = 내구도, 무게
계란을 치면 상대 계란의 무게만큼 내구도 깎임
내구도가 0이 되면 깨짐
예를들어
(7, 5) (3, 4)
1로 2를 치면 (3, 5) (-2, 4)

* 풀이
왼쪽부터 차례대로 들어서 한 번 씩만 다른 계란을 쳤을 때 최대한 많은 계란 깨기
무조건 내구도 조금 남은 계란을 고르는 식으론 풀 수 없음.
해 봐야 앎.
! 틀림
깰 수 있는 계란이 없을 때만 안깨고 넘어갈 수 있음 -> 깨지는거 체크 if문 안에서 안해서 틀림
"""

num_of_eggs = int(input())
D, W = 0, 1
eggs = [list(map(int, input().split())) for _ in range(num_of_eggs)]

ans = 0


def go(egg, broken):
    if egg == num_of_eggs:
        global ans
        ans = max(ans, broken)
        return
    # 백트래킹 - 현재 정답을 넘을 가능성이 있는 지
    breakable = (num_of_eggs - egg) * 2  # 현재 남은 게 다 깨진다면
    if broken + breakable < ans:
        return
    # 이미 깨짐
    if eggs[egg][D] <= 0:
        go(egg + 1, broken)
        return
    can_break_other = False
    for other in range(num_of_eggs):
        if other == egg:
            continue
        if eggs[other][D] > 0:
            can_break_other = True
            # 계란 깨기
            eggs[other][D] -= eggs[egg][W]
            eggs[egg][D] -= eggs[other][W]
            # 깨진거 탐색
            new_broken = 1 if eggs[egg][D] <= 0 else 0
            new_broken += 1 if eggs[other][D] <= 0 else 0
            # 다음 계란 탐색
            go(egg + 1, broken + new_broken)
            # 나머지 탐색을 위해 원상복구
            eggs[other][D] += eggs[egg][W]
            eggs[egg][D] += eggs[other][W]
    # 만약 칠 수 있는 계란이 없었다면
    if not can_break_other:
        go(egg + 1, broken)


go(egg=0, broken=0)
print(ans)
