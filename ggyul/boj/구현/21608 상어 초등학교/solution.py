'''
https://www.acmicpc.net/problem/21608
상어 초등학교
'''

n = int(input())
prefer = [0]*(n*n+1)
orders = []
for _ in range(n*n):
    student, *likes = map(int, input().split())
    prefer[student] = likes
    orders.append(student)


class Seat:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.student = 0


seats = []
for i in range(n):
    for j in range(n):
        seats.append(Seat(i, j))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def count_like(seat, student):
    if seat.student > 0:
        return -1
    count = 0
    for i in range(4):
        nx = seat.r + dx[i]
        ny = seat.c + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            next = seats[nx*n+ny]
            if next.student in prefer[student]:
                count += 1
    return count


def count_empty(seat):
    count = 0
    for i in range(4):
        nx = seat.r + dx[i]
        ny = seat.c + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            next = seats[nx*n+ny]
            if next.student == 0:
                count += 1
    return count


for order in orders:
    seat = max(seats, key=lambda seat: (
        count_like(seat, order), count_empty(seat), -seat.r, -seat.c)
    )
    seat.student = order

score = 0
for seat in seats:
    count = 0
    for i in range(4):
        nx = seat.r + dx[i]
        ny = seat.c + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            next = seats[nx*n+ny]
            if next.student in prefer[seat.student]:
                count += 1
    score += int(1*(10**(count-1)))
print(score)
