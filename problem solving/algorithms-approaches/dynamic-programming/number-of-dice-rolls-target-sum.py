'''
    problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum
    concepts: Dynamic Programming, Bounded Knapsack, DP Cache
    performance: 80.79% runtime, 18.77% memory
'''
from functools import cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        @cache
        def getNumWays(diceCount, curTarget):
            if diceCount >= n:
                return int(curTarget == 0)
            if curTarget <= 0:
                return 0
            numWays = 0
            for i in range(1, k+1):
                
                numWays += getNumWays(diceCount+1, curTarget-i)
            return numWays%MOD
        return getNumWays(0, target)