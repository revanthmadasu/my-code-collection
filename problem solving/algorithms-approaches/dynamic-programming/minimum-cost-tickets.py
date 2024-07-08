'''
    problem: https://leetcode.com/problems/minimum-cost-for-tickets
    concepts: Dynamic Programming, 0/1 Knapsack, DP Cache
    performance: 98.8% runtime, 17.23% memory
'''
from typing import List
from functools import cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def getMinCost(i):
            if i >= len(days):
                return 0
            # print(f'visiting {i}')
            day1PassCost = costs[0] + getMinCost(i+1)
            day7Exp = i
            while day7Exp < len(days) and days[day7Exp] < days[i] + 7:
                day7Exp += 1
            day7PassCost = costs[1] + getMinCost(day7Exp)
            day30Exp = i
            while day30Exp < len(days) and days[day30Exp] < days[i] + 30:
                day30Exp += 1
            day30PassCost = costs[2] + getMinCost(day30Exp)
            return min(day1PassCost, day7PassCost, day30PassCost)
        return getMinCost(0)