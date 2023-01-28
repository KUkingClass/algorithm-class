import sys

days = int(input())
time_profit = [list(map(int, sys.stdin.readline().split())) for _ in range(days)]
max_profit = [0] * (days + 1)
for day in range(days):
    if day >= 1:
        max_profit[day] = max(max_profit[day], max_profit[day - 1])
    end_day = day + time_profit[day][0]
    if end_day > days:
        continue
    max_profit[end_day] = max(max_profit[end_day], max_profit[day] + time_profit[day][1])
print(max(max_profit[days], max_profit[days - 1]))
