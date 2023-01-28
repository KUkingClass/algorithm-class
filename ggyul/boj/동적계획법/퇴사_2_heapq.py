import sys
import heapq

days = int(input())
start_days = []
profits = []
for day in range(days):
    time, profit = map(int, sys.stdin.readline().split())
    end_day = day + time
    heapq.heappush(start_days, (end_day, (day, end_day)))
    profits.append(profit)

max_profit = [0] * (days + 1)
for day in range(1, days + 1):
    max_profit[day] = max_profit[day - 1]
    while start_days[0][1][1] == day:
        start_day = heapq.heappop(start_days)[1][0]
        max_profit[day] = max(max_profit[day], max_profit[start_day] + profits[start_day])
print(max_profit[days])
