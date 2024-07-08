'''
    problem: https://leetcode.com/problems/coin-change-ii/
    concepts: Dynamic Programming, Unbounded Knapsack, DP Cache
    performance: 9.07% runtime, 19.83% memory
'''
from typing import List
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def numWays(i, amount):
            if i >= len(coins) and amount > 0:
                return 0
            if amount == 0:
                return 1
            tAmount = amount
            curWays = numWays(i+1, tAmount)
            while tAmount >= coins[i]:
                tAmount -= coins[i]
                curWays += numWays(i+1, tAmount)
            return curWays
        return numWays(0, amount)