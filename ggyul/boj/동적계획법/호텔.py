"""
https://www.acmicpc.net/problem/1106
호텔
"""

customer_goal, city_count = map(int, input().split())
costs = []
people = []
for _ in range(city_count):
    cost, person = map(int, input().split())
    costs.append(cost)
    people.append(person)
dp = [0] * (customer_goal + 1)


def get_before_cost(customer, city):
    if customer - people[city] >= 0:
        return dp[customer - people[city]]
    else:
        return 0


for customer in range(1, customer_goal + 1):
    dp[customer] = \
        min(get_before_cost(customer, city) + costs[city] for city in range(city_count))

print(dp[customer_goal])