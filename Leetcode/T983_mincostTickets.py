"""
You have planned some train traveling one year in advance.
The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
Train tickets are sold in three different ways:
    a 1-day pass is sold for costs[0] dollars,
    a 7-day pass is sold for costs[1] dollars, and
    a 30-day pass is sold for costs[2] dollars.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11

Constraints:
    1 <= len(days) <= 365
    1 <= days[i] <= 365
    days is in strictly increasing order.
    len(costs) == 3
    1 <= costs[i] <= 1000
"""


def minCostTickets(days, costs):
    """DP Bottom up"""
    n = len(days)
    dp = [0] * (days[-1] + 1)

    for i in range(1, len(dp)):
        if i in days:
            dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
        else:
            dp[i] = dp[i - 1]

    return dp[-1]


days = [1, 4, 6, 7, 8, 9, 13, 20]
costs = [2, 7, 15]
print(minCostTickets(days, costs))
