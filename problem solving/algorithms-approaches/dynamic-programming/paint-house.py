'''
    problem: https://leetcode.com/problems/paint-house/
    concepts: dynamic programming, arrays
    performance: 93.36% runtime, 62.57% memory
'''
from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        r,b,g = 0,0,0
        for cost in costs:
            r,b,g = min(b,g) + cost[0], min(r,g) + cost[1], min(r,b) + cost[2]
        return min(r,b,g)