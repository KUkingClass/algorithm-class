import sys

if __name__ == '__main__':
    n, duration, fine_per_minute = sys.stdin.readline().split()
    n, fine_per_minute = map(int, [n, fine_per_minute])
    base_day, base_time = duration.split("/")
    base_day = int(base_day)
    base_hour, base_minute = map(int, base_time.split(":"))

    rental_book = {}
    day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    answer = {}

    for _ in range(n):
        calendar, time, item, userid = sys.stdin.readline().split()
        year, month, day = map(int, calendar.split("-"))
        hour, minute = map(int, time.split(":"))
        item = item.upper()  # aa aaa12 와 aaa aa12 구별을 위해

        minutes_from_dayone = (sum(day_of_month[:month]) + day - 1) * 24 * 60 + hour * 60 + minute
        if item + userid in rental_book:
            rental_time = minutes_from_dayone - rental_book[item + userid]
            times_over = rental_time - (base_day * 24 * 60 + base_hour * 60 + base_minute)
            if times_over > 0:
                answer[userid] = answer.get(userid, 0) + times_over * fine_per_minute
            rental_book.pop(item + userid)  # 똑같은 유저가 똑같은 상품을 여러 번 빌릴 수 있으므로 반납하면 딕셔너리에서 빼야함
        else:
            rental_book[item + userid] = minutes_from_dayone

    if not answer:
        print(-1)
    else:
        for key, val in sorted(answer.items()):
            print(key, val)
