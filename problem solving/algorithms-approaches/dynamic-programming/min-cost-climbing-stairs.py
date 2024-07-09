'''
    problem: https://leetcode.com/problems/min-cost-climbing-stairs/
    concepts: dynamic programming, Fibanocci Dp pattern
    performance: 83.54% runtime, 29.39% memory
'''
'''
[1,100,1,1,1,100,1,1,100,1]
[6,105,5,5,4,102,3,2,100,1]
'''
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])