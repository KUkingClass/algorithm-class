import sys
from collections import defaultdict

days = int(input())
start_days = defaultdict(list)
profits = []
for day in range(days):
    time, profit = map(int, sys.stdin.readline().split())
    start_days[day + time].append(day)
    profits.append(profit)
max_profit = [0] * (days + 1)
for day in range(1, days + 1):
    max_profit[day] = max_profit[day - 1]
    for start_day in start_days[day]:
        max_profit[day] = max(max_profit[day], max_profit[start_day] + profits[start_day])

print(max_profit[days])
