'''
    problem: https://leetcode.com/problems/ones-and-zeroes/
    concepts: Dynamic Programming, 0/1 Knapsack, DP Cache
    performance: 86.64% runtime, 27.59% memory
'''
from typing import List
from functools import cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def getCountPair(b_str):
            zC = 0
            oC = 0
            for ch in b_str:
                if ch == '0':
                    zC += 1
                else:
                    oC += 1
            return (zC, oC)
        pairs = [getCountPair(b_str) for b_str in strs]
        @cache
        def dp(i, r):
            curPairAllowed = r[0] >= pairs[i][0]  and r[1] >= pairs[i][1]
            if i+1 >= len(pairs):
                return int(curPairAllowed)
            withPair = 0
            if curPairAllowed:
                withPair = 1 + dp(i+1, (r[0] - pairs[i][0], r[1] - pairs[i][1]))
            withoutPair = dp(i+1, r)
            return max(withPair, withoutPair)
        return dp(0, (m,n))
            