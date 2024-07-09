'''
    problem: https://leetcode.com/problems/coin-change-ii/
    concepts: Dynamic Programming, Unbounded Knapsack, DP Tabulation, DP Cache
    performance: 39.30% runtime, 58.06% memory
'''
from typing import List
from functools import cache
#tabulation approach - better than caching
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for r in range(len(coins)):
            dp[r][amount] = 1
        for r in range(len(coins)-1, -1, -1):
            for c in range(amount-1, -1,-1):
                curAmount = amount - c
                # amI = amount - i
                amI = amount - curAmount + coins[r]
                numWays = 0
                # print(f'{r}, {c}, {amI}, {curAmount}')
                dp[r][c] = dp[r+1][c] + (dp[r][amI] if curAmount - coins[r] >= 0 else 0)
        return dp[0][0]

# cache approach - performance: 9.07% runtime, 19.83% memory
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         @cache
#         def numWays(i, amount):
#             if i >= len(coins) and amount > 0:
#                 return 0
#             if amount == 0:
#                 return 1
#             tAmount = amount
#             curWays = numWays(i+1, tAmount)
#             while tAmount >= coins[i]:
#                 tAmount -= coins[i]
#                 curWays += numWays(i+1, tAmount)
#             return curWays
#         return numWays(0, amount)