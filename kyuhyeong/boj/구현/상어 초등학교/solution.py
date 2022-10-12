import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    students = {}
    for _ in range(n**2):
        sid, f1, f2, f3, f4 = map(int, sys.stdin.readline().split())
        students[sid] = [f1, f2, f3, f4]

    seats = [[0 for _ in range(n)] for _ in range(n)]

    for sid, val in students.items():
        best_i, best_j, max_favorites, max_blank = 0, 0, -1, -1
        for i in range(n):
            for j in range(n):
                if seats[i][j]:
                    continue

                cur_favorites = 0
                cur_blank = 0
                if i > 0:
                    if seats[i-1][j] in val:
                        cur_favorites += 1
                    elif not seats[i-1][j]:
                        cur_blank += 1
                if j > 0:
                    if seats[i][j-1] in val:
                        cur_favorites += 1
                    elif not seats[i][j-1]:
                        cur_blank += 1
                if j < n - 1:
                    if seats[i][j+1] in val:
                        cur_favorites += 1
                    elif not seats[i][j+1]:
                        cur_blank += 1
                if i < n - 1:
                    if seats[i+1][j] in val:
                        cur_favorites += 1
                    elif not seats[i+1][j]:
                        cur_blank += 1

                if cur_favorites > max_favorites or (cur_favorites == max_favorites and max_blank < cur_blank):
                    best_i, best_j, max_favorites, max_blank = i, j, cur_favorites, cur_blank

        seats[best_i][best_j] = sid

    total_score = 0
    score = [0, 1, 10, 100, 1000]
    for i in range(n):
        for j in range(n):
            favorites = students[seats[i][j]]
            count = 0
            if i > 0 and seats[i-1][j] in favorites:
                count += 1
            if j > 0 and seats[i][j-1] in favorites:
                count += 1
            if j < n - 1 and seats[i][j+1] in favorites:
                count += 1
            if i < n - 1 and seats[i+1][j] in favorites:
                count += 1
            total_score += score[count]

    print(total_score)
