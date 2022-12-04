def solution(places):
    answer = [0 for _ in range(5)]

    for idx, place in enumerate(places):
        applicants = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    applicants.append((i, j))

        answer[idx] = check(place, applicants)

    return answer


def check(place, applicants):
    for i in range(len(applicants) - 1):
        x1, y1 = applicants[i]
        for j in range(i + 1, len(applicants)):
            x2, y2 = applicants[j]
            distance = abs(x2 - x1) + abs(y2 - y1)
            if distance == 1:   # 지원자끼리 붙어있으면 바로 아웃
                return 0
            elif distance == 2:
                if x1 == x2:    # 같은 라인에 위치
                    if place[x1][min(y1, y2) + 1] != "X":
                        return 0
                elif y1 == y2:
                    if place[min(x1, x2) + 1][y1] != "X":
                        return 0
                elif place[min(x1, x2)][y2] != "X" or place[max(x1, x2)][y1] != "X":  # 대각선에 위치
                    return 0
    return 1


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
